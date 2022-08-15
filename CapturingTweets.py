# The Author of this project is Majid Khan.
# For this Project you will need to have access to twitter Developer account in order to use keys.
# i will not provide my own keys, you will need to have your own...just apply for twitter developer account.

import tweepy
import configparser
import pandas as pd

# i'm reading keys from "Config.ini" file thats why I wrote this code
config = configparser.ConfigParser()
config.read('config.ini')

# Enter all your keys in the config.ini
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Twitter Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
api = tweepy.API(auth)

# searching for specific key Word
keyword = 'sad'

# setting the limit of tweets to retrive
limit =300
tweets = tweepy.Cursor(api.search_tweets, q = keyword, count= 100, tweet_mode = 'extended').items(limit)

# to search tweets for specific user just comment above line and uncomment the below line of code
# tweets = api.user_timeline(screen_name = user, count= limit, tweet_mode = 'extended')

# coloumns to get from tweets, In this case we have user namer and the actual tweet
columns = ['User', 'Tweet']
data = []
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)
print(df)