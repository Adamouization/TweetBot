#!/usr/bin/env python
# imports
import keys
import sys
#import tweepy
import os
import random
from twython import Twython

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# authentication to twitter application using local keys
#auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
#auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)
#api = tweepy.API(auth)
api = Twython(keys.CONSUMER_KEY,keys.CONSUMER_SECRET,keys.ACCESS_KEY,keys.ACCESS_SECRET)

# retrieve CPU temperature
#cmd = '/opt/vc/bin/vcgencmd measure_temp'
#line = os.popen(cmd).readline().strip()
#temp = line.split('=')[1].split("'")[0]

# tweet random sentences retrieved from a txt file
def randomTweet():
	try:
		tweetsFile = open(os.path.join(__location__,'tweets.txt'),'r')
		tweetsList = tweetsFile.readlines()
		tweetsFile.close()
		randomChoice = random.randrange(len(tweetsList))
		print(tweetsList[randomChoice]) #debugging
		api.update_status(status=tweetsList[randomChoice])
		return None
	except IOError:	
		return None

randomTweet()

# update twitter status
#api.update_status(status='My current Raspberry Pi CPU temperature is ' + temp + ' C')
#api.update_status(sys.argv[1])
