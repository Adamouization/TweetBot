#!/usr/bin/env python
import sys
import tweepy
CONSUMER_KEY = 'Skn7K6EscqGwlqNE7YFvugFHv'
CONSUMER_SECRET = 'FO2RvQG9sTgyuMx5fYs1XLL65B3yiYBTTxf1f4YcbpSlAfg1MY'
ACCESS_KEY = '825827462038880261-jg5OQZxmMjFPcNDWhwNL0XJ6lx24DtD'
ACCESS_SECRET = 'rxR7RveK8ECbP6UVkzQTltUkqlM5L3QxluG6gUiETUf1p'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])
