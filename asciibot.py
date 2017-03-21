# This is a twitter bot

# import secret keys
# from keys import my_secret
import base64
import os
import random
import urllib.request

# from io import BytesIO
# from imageserv import image02
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

# with urllib.request.urlopen('https://shirtfactory.herokuapp.com/design/image/37') as img_raw:
    # print(type(img_raw))

design_nums = [1, 2, 3, 4, 5, 7, 22, 27, 34, 35, 36, 37, 39, 41, 42, 43, 45, 46, 47, 48, 49]

link_num = random.choice(design_nums)

link = 'https://shirtfactory.herokuapp.com/design/image/' + str(link_num)

## get bytecode from shirtfactory.heroku
# with urllib.request.urlopen('https://shirtfactory.herokuapp.com/design/image/2') as img_raw:
#     img_bytes = img_raw.read()
with urllib.request.urlopen(link) as img_raw:
    img_bytes = img_raw.read()

# print('______raw read results below_______')
# print(type(img_bytes))
# print(img_bytes[0:30])

# print('__trying b64 encoding on raw bytes_')
img_str_b64_encoded = base64.b64encode(img_bytes)
img_str_b64_decoded = img_str_b64_encoded.decode()
# print(type(img_str_b64_encoded))
# print(img_str_b64_decoded[0:30])

# print('___________output below_______')
img_str_b64_decoded_str = str(img_str_b64_decoded)
# print(type(img_str_b64_decoded_str))
# print(img_str_b64_decoded_str[0:30])


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
response = twitter.upload_media(media=img_str_b64_decoded_str)
#
twitter.update_status(status='ASCII design number ' + str(link_num), media_ids=[response['media_id']])

# response = twitter.upload_media(media_data='https://shirtfactory.herokuapp.com/design/image/46')
