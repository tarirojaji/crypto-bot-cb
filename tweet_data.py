from os import access
import tweepy
import textblob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from datetime import datetime, timedelta

plt.style.use('seaborn')

# access keys by each lines
all_keys = open('tweetkeys', 'r').read().splitlines()

api_key = all_keys[0]
api_key_sec = all_keys[1]
acc_token = all_keys[2]
acc_token_sec = all_keys[3]

# authenticate the twitter api
auth_twt = tweepy.OAuthHandler(api_key,api_key_sec)
auth_twt.set_access_token(acc_token, acc_token_sec)

api = tweepy.API(auth_twt, wait_on_rate_limit=True)

crypto_currency = 'Bitcoin'

end = "2021-09-26"

search = f'#{crypto_currency} -filter:retweets'

# return tweets in extended mode
tweet_cursor = tweepy.Cursor(api.search_tweets, q=search, lang='en', until=end, tweet_mode='extended',).items(100)

tweets = [tweet.full_text for tweet in tweet_cursor]

# create dataframe for all the tweets
tweets_df = pd.DataFrame(tweets, columns=['Tweets'])

# clean tweets by replacing unwanted text eg, links, hashtags, mentions and new lines
for _, row in tweets_df.iterrows():
    row['Tweets'] = re.sub('http\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('#\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('@\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('\\n', '', row['Tweets']) 

    # print(row['Tweets'])

# collect polarity scores of tweets and match them to positives(+0) and negatives(-0)
tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol: '+' if pol > 0 else '-' )

positive = tweets_df[tweets_df.Result == '+'].count()['Tweets']
negative = tweets_df[tweets_df.Result == '-'].count()['Tweets']

# print(positive, negative)

plt.bar([0,1], [positive, negative], label=['Positive', 'Negative'], color=['green', 'red'])
plt.legend()

# plt.scatter([0,1], [positive, negative], label=['Positive', 'Negative'], color=['green', 'red'])

plt.show()

# def perc():
#     if positive > negative:
#         diff = ((positive-negative)/((positive+negative)/2))*100
#     print(diff)

# perc()

