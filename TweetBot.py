# TweetBot
# @author: Adam Jaamour
# @email: adam@jaamour.com
# @version: 2.1
# @date: 19/02/2017

# imports
import keys                     # authentification to twitter app
import sys                      # used to retrieve CPU temp
import os
import random                   # used to generate random numbers
import tweepy                   # used to connect to twitter app
from datetime import datetime   # used to get the current time


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


# authentication to twitter application using locally-stored keys and tweepy
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
		#print('length of list = ' + str(len(tweetsList)-1)) #debugging
		
		# select a tweet from txt file
		randomChoice = random.randrange(len(tweetsList))
		tweet0 = tweetsList[randomChoice]

		# update twitter status if tweet is within character limit
		if len(tweet0) <= 140:
			api.update_status(status = tweet0)
			print('tweeting: ' + tweet0)
			temp_tweet0 = now + tweet0
			updateLog(tweet0)
		else:
			print('tweet not sent: too long (140 chars max)')
			error = now + "Tweet not sent"
			updateLog(error)
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
        picture_path_temp = '/home/pi/Documents/PythonProjects/TweetBot/pictures/' + pic_name
        print("pic number: temperature" + str(random_cpu_pic))

        # generate tweet to send with time, temp and degree symbol
        tweet1 = now + ' My current CPU temperature is ' + temp + ' ' + degree + 'C'

        # tweet CPU temp
        api.update_with_media(picture_path_temp, status = tweet1)
        print('tweeting : ' + tweet1 + 'with pic: temperature' + str(random_cpu_pic))

        # update log
        temp_tweet1 = now + ' My current CPU temperature is ' + temp + ' C\n' # without degree symbol
        updateLog(temp_tweet1)


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
                print('tweeting : ' + tweet2)

                # update log
                updateLog(tweet2)

                return None
        except IOError:
                return None


# update log
def updateLog(tweet):
        log_entry = "tweeted at: " + now + " the following message: " + tweet
        try:
                fo = open("log.txt", "rw+")
                # write line at end of the file
                fo.seek(0,2)
                fo.write(log_entry)
                fo.close()
                print('successfully updated log')
                
                return None
        except IOError:
                return None

        
# script
randomTweet = random.randrange(3)
if randomTweet == 0:
        print("0: random tweet generated")
        statusTweet()
elif randomTweet == 1:
        print("1: CPU tweet generated")
        cpuTweet()
elif randomTweet == 2:
        print("2: pic tweet generated")
        picTweet()


# tweet CLI input
#api.update_status(sys.argv[1])
