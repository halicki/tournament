-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database if exists tournament;
create database tournament;

\c tournament;

create table Players (
    name character varying(30) not null,
    player_id serial primary key
);

create table Matches (
    winner_id integer references Players(player_id),
    loser_id integer references Players(player_id),
    constraint cantBeTheSamePlayer check (winner_id != loser_id)
);

create view PlayersRank as
     select player_id, name,
            count(case when winner_id = player_id then 1 else null end) as wins,
            count(winner_id) as matches
       from Players left join Matches
         on (player_id = winner_id or player_id = loser_id)
   group by player_id
   order by wins;