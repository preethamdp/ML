import tweepy
from textblob import TextBlob
import csv

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Truimp')
with open("tweets.csv",'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['tweets','polarity','subjectivity'])
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text).sentiment
        print(analysis)
        try:
            csvwriter.writerow([tweet.text,analysis[0],analysis[1]])
        except:
            pass
        # csvwriter.writerow
