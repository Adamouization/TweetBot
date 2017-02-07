#!/usr/bin/env python
# imports
import keys
import sys
import os
import random
from twython import Twython
from datetime import datetime

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# authentication to twitter application using local keys
api = Twython(keys.CONSUMER_KEY,keys.CONSUMER_SECRET,keys.ACCESS_KEY,keys.ACCESS_SECRET)

# retrieve CPU temperature
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()

# tweet random sentences retrieved from a txt file
def randomTweet():
	try:
		tweetsFile = open(os.path.join(__location__,'tweets.txt'),'r')
		tweetsList = tweetsFile.readlines()
		tweetsFile.close()
		randomChoice = random.randrange(len(tweetsList))
		#if tweetsList[randomChoice] <= 140:
		print(tweetsList[randomChoice]) #debugging
		api.update_status(status=tweetsList[randomChoice]) #update twitter status
		#api.update_status(status=tweetsList[15]) #specific item in array
		#else:
		#print "tweet not sent: too long (140 chars max)"
		return None
	except IOError:	
		return None

# tweet
randomTweet()

#api.update_status(sys.argv[1]) #tweet line input
