# This is a twitter bot

# import secret keys
# from keys import my_secret
import os

# Importing the module
from twython import Twython

# change these when app is running on heroku w/ environmental variables
# app_key = my_secret.app_key
# app_secret = my_secret.app_secret
# oauth_token = my_secret.oauth_token
# oauth_token_secret = my_secret.oauth_token_secret

app_key = os.environ['APP_KEY']
app_secret = os.environ['APP_SECRET']
oauth_token = os.environ['OAUTH_TOKEN']
oauth_token_secret = os.environ['OAUTH_TOKEN_SECRET']

# Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
# The above should just be a single line, without the break

# The obligatory first status update to test
twitter.update_status(status=chr(128123) + 'Heroku works' + chr(128123))
