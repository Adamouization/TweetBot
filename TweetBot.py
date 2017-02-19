#!/usr/bin/env python
# imports
import keys                     # authentification to twitter app
import sys                      # used to retrieve CPU temp
import os
import random                   # used to generate random numbers
import tweepy                   # used to connect to twitter app
from datetime import datetime   # used to get the current time


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


# authentication to twitter application using locally-stored keys
auth = tweepy.OAuthHandler(
	keys.CONSUMER_KEY, 
	keys.CONSUMER_SECRET
)
auth.set_access_token(
	keys.ACCESS_KEY, 
	keys.ACCESS_SECRET
)
api = tweepy.API(auth)


# time
i = datetime.now()
now = i.strftime('%Y/%m/%d %H:%M:%S')


# tweet random sentences retrieved from a txt file
def statusTweet():
	try:
		# read txt file
		tweetsFile = open(os.path.join(__location__,'tweets.txt'),'r')
		tweetsList = tweetsFile.readlines()
		tweetsFile.close()
		#print('length of list = ' + str(len(tweetsList)-1))
		
		# select a tweet from txt file
		randomChoice = random.randrange(len(tweetsList))
		tweet0 = tweetsList[randomChoice]

		# update twitter status if tweet is within character limit
		if len(tweet0) <= 140:
			print(tweet0) #debugging
			api.update_status(status = tweet0)
			#api.update_status(status=tweetsList[15]) #specific item in array (debugging)
		else:
			print "tweet not sent: too long (140 chars max)"
		return None
	except IOError:	
		return None


# tweet CPU temperature along with a jpeg picture
def cpuTweet():
        # retrieve CPU temperature
        degree = unichr(176) #degree symbol
        cmd = '/opt/vc/bin/vcgencmd measure_temp'
        line = os.popen(cmd).readline().strip()
        temp = line.split('=')[1].split("'")[0]
        
        # picture
        random_cpu_pic = random.randrange(0,3)
        pic_name = "temperature" + str(random_cpu_pic) +  ".jpg"
        picture_path = '/home/pi/Documents/PythonProjects/TweetBot/pictures/' + pic_name
        print("pic number: temperature" + str(random_cpu_pic))

        # generate tweet to send with time, temp and degree symbol
        tweet1 = now + ' My current CPU temperature is ' + temp + ' ' + degree + 'C'

        # tweet CPU temp
        api.update_with_media(picture_path, status = tweet1)


# tweet a picture along with its relevant status
def picTweet():
        try:
                # status
                PicStatusFile = open(os.path.join(__location__, 'pic_status.txt'), 'r')
                tweetsPicList = PicStatusFile.readlines()
                PicStatusFile.close()
                randomPicChoice = random.randrange(len(tweetsPicList))
                tweet2 = tweetsPicList[randomPicChoice]

                # picture
                pic_name = "tweetpic" + str(randomPicChoice) + ".jpg"
                picture_path = '/home/pi/Documents/PythonProjects/TweetBot/pictures/' + pic_name
                print("pic #: tweetpic" + str(randomPicChoice))

                # tweet
                api.update_with_media(picture_path, status = tweet2)
                return None
        except IOError:
                return None
        


randomTweet = random.randrange(3)
if randomTweet == 0:
        #statusTweet()
        print(0)
elif randomTweet == 1:
        #cpuTweet()
        print(1)
elif randomTweet == 2:
        #picTweet()
        print(2)


# update log
#fo = open("log.txt", "rw+")
#print "Name of the file: ", fo.name
# write line at end of the file
#fo.seek(0,2)
#fo.write(tweet)
#fo.close()


# tweet CLI input
#api.update_status(sys.argv[1])
