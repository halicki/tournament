#!/usr/bin/env python3
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from functools import wraps


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def connected(func):
    """Handles connection. Provides self.cursor"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        with connect() as db:
            with db.cursor() as cursor:
                return func(db, cursor, *args, **kwargs)

    return wrapper


@connected
def delete_matches(db, cursor):
    """Remove all the match records from the database."""
    cursor.execute("delete from Matches *;")
    db.commit()


@connected
def delete_players(db, cursor):
    """Remove all the player records from the database."""
    cursor.execute("delete from Players *;")
    db.commit()


@connected
def count_players(db, cursor):
    """Returns the number of players currently registered."""
    cursor.execute("select count(*) count from Players;")
    return int(cursor.fetchone()[0])


@connected
def register_player(db, cursor, name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    if not name or not isinstance(name, str):
        raise ValueError("Need a valid full name.");
    cursor.execute('insert into Players (name) values (%s);', (name,))
    db.commit()


@connected
def player_standings(db, cursor):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    cursor.execute("select * from PlayersRank")
    return cursor.fetchall()


@connected
def report_match(db, cursor, winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    cursor.execute("insert into Matches (winner_id, loser_id) "
                   "values (%s, %s);", (winner, loser,))
    db.commit()


@connected
def swiss_pairings(db, cursor):
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    cursor.execute("""
          with PlayersRankWithColumn as (
                   select player_id, name,
                          row_number() over () as rn
                     from PlayersRank
               )
        select first.player_id, first.name, second.player_id, second.name
          from PlayersRankWithColumn as first
    inner join PlayersRankWithColumn as second
            on first.rn+1 = second.rn and first.rn % 2 = 1;""")
    return cursor.fetchall()



