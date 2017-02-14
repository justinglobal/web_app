# This is a twitter bot

# import secret keys
# from keys import my_secret
import os
import urllib.request
import base64
from io import BytesIO

from imageserv import image02
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
# twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
# The above should just be a single line, without the break

# with urllib.request.urlopen('https://shirtfactory.herokuapp.com/design/image/37') as img_raw:
    # print(type(img_raw))


## get bytecode from shirtfactory.heroku
with urllib.request.urlopen('https://shirtfactory.herokuapp.com/design/image/37') as img_raw:
    img_bytes = img_raw.read()

print('__trying b64 encoding on raw bytes_')
img_str_b64_encoded = base64.b64encode(img_bytes)
print(img_str_b64_encoded)


# print(img_bytes[0:30])
#
# img_d64 = base64.b64decode(img_bytes)
#
# print(type(img_d64))
# img_d64_str = str(img_d64)
# print(img_d64_str[0:30])
# print('___________________')
#
# ## convert img_code from bytes to string
# img_str = str(img_bytes)
#
# print(type(img_str))
# print(img_str[0:30])

print('______________________________')

print(type(image02))
print(image02[0:30])
# check if img_code needs to be a list

# def makemsg(message):
#     """function to make message?"""
#     return

# The obligatory first status update to test
# twitter.update_status(status=chr(128079) + 'Heroku check 7' + chr(128079))

# twitter.update_status(status=image01)

# img = twitter.request('https://shirtfactory.herokuapp.com/design/image/46').read()
# response = twitter.upload_media(media=img)
# response = twitter.upload_media(media_data=img)

# this is current code below:
# response = twitter.upload_media(media=img_str)
# #
# twitter.update_status(status='image check 04', media_ids=[response['media_id']])

# response = twitter.upload_media(media_data='https://shirtfactory.herokuapp.com/design/image/46')
