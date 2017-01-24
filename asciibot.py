# This is a twitter bot

# import secret keys
from keys import my_secret

# Importing the module
from twython import Twython

# change these when app is running on heroku w/ environmental variables
app_key = my_secret.app_key
app_secret = my_secret.app_secret
oauth_token = my_secret.oauth_token
oauth_token_secret = my_secret.oauth_token_secret

# Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
# The above should just be a single line, without the break

# The obligatory first status update to test
twitter.update_status(status=chr(128123) + "Follow JustinCybertron on Instagram for more digital art!" + chr(128123))
