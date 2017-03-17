# Tournament

## Setup
Depending on your system, setup process would be different. Please find below 
instructions how to setup system in 

#### On Ubuntu 16.04 LTS
1. Install and configure PostgreSQL
   
   Detailed info can be founde here: 
   [How To Install and Use PostgreSQL on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04).
   But here we will show the most important stuff in a succinct way.
   
   Install `postgresql` packgare:

       sudo apt-get install postgresql
   
   Create a postgres role
    
       sudo -u postgres createuser {your_username} -s 
    
   From now on you can use your own account for managing databases. Read file
   `tournament.sql` in order to setup databases.
    
       psql postgres --file=tournament.sql
       
2. Optional: Setup virtualenv

   I marked this part optional, but in my opinion it should be mandatory.
    
       virtualenv --python=python3.6 venv
       . venv/bin/activate
       
3. Install required python packages 
       
       pip install -r requirements.txt