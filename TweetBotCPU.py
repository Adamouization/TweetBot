#!/usr/bin/env python
# imports
import keys
import sys
import os
import random
from twython import Twython
from datetime import datetime

i = datetime.now()
degree = unichr(176) # degree symbol
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# authentication to twitter application using local keys
api = Twython(keys.CONSUMER_KEY,keys.CONSUMER_SECRET,keys.ACCESS_KEY,keys.ACCESS_SECRET)

# time
now = i.strftime('%Y/%m/%d %H:%M:%S')
# retrieve CPU temperature
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

api.update_status(status= now + 'My current CPU temperature is ' + temp + ' ' + degree + 'C') #tweet cpu temp
