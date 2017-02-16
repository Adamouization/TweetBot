# @ThePiTweetBot

### Features

- randomised tweets retrieved from a text file
- 140 characters limit
- tweepy API
- automatic script running using crontab
```
sudo crontab -e

*/60 * * * * python TweetBot.py
0 */3 * * * python TweetBotCPU.py

sudo crontab
```

Follow me on [Twitter](https://twitter.com/ThePiTweetBot)
