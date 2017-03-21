# Tournament

## Setup
Depending on your system, setup process would can differ. Please find below instructions how to setup system.

The project needs Python 3.6 and PostgreSQL.

1. Install and configure PostgreSQL

   Detailed info can be founde here: 
   [How To Install and Use PostgreSQL on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04).
   But here we will show the most important stuff in a succinct way.

   1. Installation 
      * On macOS, use `brew`:

            brew install postgresql

      * On Ubuntu 16.04 LTS, using a package manager of your choice, eq. `apt-get`:

            sudo apt-get install postgresql

   2. (Ubuntu) Create a postgres role

          sudo -u postgres createuser {your_username} -s

      From now on you can use your own account for managing databases. 

   3. Read file `tournament.sql` in order to setup databases.

          psql postgres --file=tournament.sql

2. Optional: Setup virtualenv

   I marked this part optional, but in my opinion it should be mandatory. It will sparate your host packages from this 
   project requirements.

   You can choose from:

   * Install `virtualenv`:

         virtualenv --python=python3.6 venv

   * or use built in module `venv`:

         python3 -m venv venv

    Now you can activate your newly created virtual environment:

       . venv/bin/activate


3. Install required python packages 

       pip install -r requirements.txt

4. Run tests!

       python tournament_test.py

## License

This  repository can be distributed in accordance to MIT License.