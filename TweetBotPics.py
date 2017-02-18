#!/usr/bin/env python

# imports
import keys
import os
import random
import tweepy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# authentification to twitter application using local keys
auth = tweepy.OAuthHandler(
    keys.CONSUMER_KEY,
    keys.CONSUMER_SECRET
)
auth.set_access_token(
    keys.ACCESS_KEY,
    keys.ACCESS_SECRET
)
api = tweepy.API(auth)

# status
tweetsFile = open(os.path.join(__location__, 'pic_status.txt'), 'r')
tweetsList = tweetsFile.readlines()
tweetsFile.close()
randomChoice = random.randrange(len(tweetsList))
tweet = tweetsList[randomChoice]

# picture
pic_name = "tweetpic" + str(randomChoice) + ".jpg"
picture_path = '/home/pi/Documents/PythonProjects/TweetBot/pictures/' + pic_name
print("pic #: tweetpic" + str(randomChoice))

# tweet
api.update_with_media(picture_path, status = tweet)
