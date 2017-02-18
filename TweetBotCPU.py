#!/usr/bin/env python
# imports
import keys
import sys
import os
import random
import tweepy
from datetime import datetime

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

# time
i = datetime.now()
now = i.strftime('%Y/%m/%d %H:%M:%S')

# retrieve CPU temperature
degree = unichr(176) #degree symbol
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

# picture
random_pic = random.randrange(3)
pic_name = "temperature" + str(random_pic) +  ".jpg"
picture_path = '/home/pi/Documents/PythonProjects/TweetBot/pictures/' + pic_name
print("pic number: temperature" + str(random_pic))

# generate tweet to send with time, temp and degree symbol
tweet = now + ' My current CPU temperature is ' + temp + ' ' + degree + 'C'
print(tweet) # debugging

# update log
#fo = open("log.txt", "rw+")
#print "Name of the file: ", fo.name
# write line at end of the file
#fo.seek(0,2)
#fo.write(tweet)
#fo.close()

# tweet CPU temp
api.update_with_media(picture_path, status=tweet)
