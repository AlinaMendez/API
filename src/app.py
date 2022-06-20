import os
from dotenv import load_dotenv
import tweepy
import requests

# load the .env file variables
load_dotenv()

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')


# your app code here
client = tweepy.Client(bearer_token='BEARER_TOKEN', 
                consumer_key='CONSUMER_KEY', 
                consumer_secret='CONSUMER_SECRET', 
                access_token='ACCESS_TOKEN', 
                access_token_secret='ACCESS_TOKEN_SECRET', 
                return_type=requests.Response, 
                wait_on_rate_limit=True) # PORQUE?