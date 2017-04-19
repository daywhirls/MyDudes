#!/usr/bin/env/python

import config
import datetime
from twitter import *

# @author David Worley, david@davidworley.com
# @date 04/19/2017
# Tweetin' to my dudes

def authenticate():
	# read secure info to login to Twitter
	t = Twitter(auth=OAuth(config.token, config.token_secret, config.consumer_key, config.consumer_secret))
	return t


def tweetToMyDudes():
	# commence the majesticnes

	t = authenticate()
	today = datetime.datetime.now().strftime("%A")
	goodTweet = "It's " + today + " my dudes"
	t.statuses.update(status= goodTweet)

tweetToMyDudes()