#!/usr/bin/env python
# imports
import keys
import sys
import os
import random
import tweepy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# authentication to twitter application using local keys
auth = tweepy.OAuthHandler(
	keys.CONSUMER_KEY, 
	keys.CONSUMER_SECRET
)
auth.set_access_token(
	keys.ACCESS_KEY, 
	keys.ACCESS_SECRET
)
api = tweepy.API(auth)

# tweet random sentences retrieved from a txt file
def randomTweet():
	try:
		# read txt file
		tweetsFile = open(os.path.join(__location__,'tweets.txt'),'r')
		tweetsList = tweetsFile.readlines()
		tweetsFile.close()
		#print('length of list = ' + str(len(tweetsList)-1))
		
		# select a tweet from txt file
		randomChoice = random.randrange(len(tweetsList))
		tweet = tweetsList[randomChoice]

		# update twitter status if tweet is not too long
		if len(tweet) <= 140:
			print(tweet) #debugging
			api.update_status(status=tweet)
			#api.update_status(status=tweetsList[15]) #specific item in array (debugging)
		else:
			print "tweet not sent: too long (140 chars max)"
		
		return None
	
	except IOError:	
		return None


# tweet
randomTweet()

# tweet CLI input
#api.update_status(sys.argv[1])
