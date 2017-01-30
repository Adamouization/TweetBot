#!/usr/bin/env python
import keys
import sys
import tweepy
import os

auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_KEY, keys.ACCESS_SECRET)

api = tweepy.API(auth)
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
api.update_status(status='My current Raspberry Pi CPU temperature is ' + temp + ' C')
#api.update_status(sys.argv[1])
