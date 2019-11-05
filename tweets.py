#!/usr/bin/python
# coding=utf-8

import tweepy
import pandas as pd
import csv  # Import csv

tweetsIds = []  # the list containing the tweet ids
tweets = []  # the list containing the tweets

# opening the csv file  and getting the twitter id coloumns
csvfile = open('get_tweets.csv', encoding="utf-8")

readCSV = csv.reader(csvfile, delimiter=',')
for row in readCSV:
    if (row and row[1] != ''):
        tweetsIds.append(row[1])

        print(tweetsIds)

auth = tweepy.auth.OAuthHandler("ntPEmjd3IqwcesLE4J8FGIggz", "MnbG735s6Q1QwhIjXHt9fsgzcJ2crQp58ohfZuHav5doEa9gm8")
auth.set_access_token("1174895695947390981-S9mbCqD8JZsVfFXeuYzYxvnzoaaJHf",
                      "jxPhX8gYGrb5QvZdsqQNN1peCqq8GSOB8SSilsKE9jJnD")

api = tweepy.API(auth)
# create a dataframe  to append tweets information
tweets_df = pd.DataFrame(columns=['ID', 'FULL TEXT', 'CREATED AT'])

for tweet in tweepy.Cursor(api.search,
                           q='පොන්න OR  පොන්නයා OR සක්කිලියා OR බඩුව  OR  වේසි OR හුත්ත OR  තම්බි OR පක OR ගණිකාව OR බැල්ලි OR බැල්ලීයො OR හලාල් OR කල්ලතෝනි OR තම්බි OR හම්බය OR තම්බියො OR හම්බයෝ OR තම්බියෝ OR හම්බයො OR හම්බිය OR හම්බියො OR හම්බියෝ OR තම්බි  OR හුකනව OR හුකපන් OR කැරි OR කිම්බ',

                           lang="si", tweet_mode='extended').items():

    if (tweet.id_str not in tweetsIds) and ('RT @' not in tweet.full_text) and (not tweet.retweeted):
        # create a dataframe from the existing information
        df = pd.DataFrame([[ tweet.id_str, tweet.full_text, tweet.created_at]],
                          columns=['ID', 'FULL TEXT', 'CREATED AT'])

        # append it to the tweets_df
        tweets_df =  tweets_df.append(df , ignore_index=True)

# ********** commented  by dj ***************
# # convert 'tweets' list to pandas.DataFrame
# tweets_df = pd.DataFrame(vars(tweets[i]) for i in range(len(tweets)))
# # define attributes you want
# tweet_atts = [
#           'id',
#           'full_text',
#           'created_at'
#       ]
# # subset dataframe
# tweets_df = tweets_df[tweet_atts]


# *********** end of comment *****************


with open('get_tweets.csv', 'a', encoding="utf-8") as f:
    tweets_df.to_csv(f, header=f.tell() == 0)