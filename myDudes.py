#!/usr/bin/env/python

import config
import datetime
import tweepy

def authenticate():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.token, config.token_secret)
    return tweepy.API(auth)

def tweetToMyDudes():
	# commence the majesticness
    api = authenticate()
    today = datetime.datetime.now().strftime("%A")
    goodTweet = "It's " + today + " my dudes"
    api.update_status(goodTweet)


tweetToMyDudes()
