#Notes for development of first web app

##Things used
1. Python + web languages
2. Django
3. PosgreSQL
4. Heroku - hosting
5. git/hub - version control and setup

5/15/2016

- set up Heroku account
  user/email: justinglobal@gmail.com
  pass: see password notes

- set up PostgreSQL on raccoonjunkbox (this computer)
  PATH installed

    raccoonjunkbox:~ admin$ psql -h localhost
    psql (9.5.2)
    Type "help" for help.

    raccoonjunkbox:~ admin$ which psql
    /Applications/Postgres.app/Contents/Versions/latest/bin/psql

- execute the following commands in your local command shell or terminal:
   $ git clone https://github.com/heroku/python-getting-started.git
   $ cd python-getting-started
   You now have a functioning git repository that contains a simple application as well as a requirements.txt file, which is used by Python’s dependency manager, Pip.
