import os
import requests 
import tweepy
import re
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')


# your app code here
client = tweepy.Client(bearer_token=bearer_token, 
                    consumer_key=consumer_key, 
                    consumer_secret=consumer_secret, 
                    return_type=requests.Response, 
                    wait_on_rate_limit=True)

query = '#100daysofcode (pandas OR python) -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['author_id','created_at','lang'], max_results=100)
tweets_json = tweets.json()
#print(tweets_json)
tweets_data = tweets_json['data']
df = pd.json_normalize(tweets_data)
print(df)

df.to_csv("coding-tweets.csv")

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

[pandas, python] = [0, 0]

for index, row in df.iterrows():
    pandas += word_in_text('pandas', row['text'])
    python += word_in_text('python', row['text'])

sns.set(color_codes=True)
cd = ['pandas', 'python']
ax = sns.barplot(cd, [pandas, python])
ax.set(ylabel="count")
