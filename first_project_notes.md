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

- prepare app
  execute the following commands in your local command shell or terminal:
   $ git clone https://github.com/heroku/python-getting-started.git
   $ cd python-getting-started
   You now have a functioning git repository that contains a simple application as well as a requirements.txt file, which is used by Python’s dependency manager, Pip.

- github repo set up but not local not initialized

- fucked up repo and github...made local directory submodule of parent

- changed runtime.txt to python 3.5.1

- created app
Creating app... done, ⬢ serene-oasis-73032
https://serene-oasis-73032.herokuapp.com/ | https://git.heroku.com/serene-oasis-73032.git

remote: Verifying deploy... done.
To https://git.heroku.com/serene-oasis-73032.git
 * [new branch]      master -> master

6/8/2016

PDXCodeguild instructor fixed my github repo

*Now deploying from new directory*

New directory - branch 'heroku-work' in /Users/admin/Python/pythonClass/shirt_factory
(old directory - web_app)

Set upstream master, github is set up

Checked default deployment url, it works still: https://serene-oasis-73032.herokuapp.com/

Plan:

update heroku-work with configs from web_app

  files to update:
    - procfile
    - runtime.txt
    - requirements.txt

concern: how will my database in heroku-work (which I think is currently SQLite) work
  with the PostgreSQL database I need

Change settings in procfile and wsgi.py to use project name not default name

Creating ⬢ shirtfactory... done
https://shirtfactory.herokuapp.com/ | https://git.heroku.com/shirtfactory.git

set up config files

remote: Verifying deploy... done.
To https://git.heroku.com/shirtfactory.git

# SITE DEPLOYED
 - so excited

deploy command line: (venv) raccoonjunkbox:shirt_factory admin$ git push heroku heroku-work:master

I will develop locally using my SQLite db with the same command: python manage.py runserver
