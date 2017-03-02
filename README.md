# @ThePiTweetBot

### Features

- dynamic randomised tweets retrieved from a text file every hour
- tweets CPU temperature at the beginning of every third hour
- tweet .jpg files
- local 140-characters message limit
- write to a log each time script is ran to keep track of tweets sent
- automatic script running using crontab:
```
sudo crontab -e

*/30 * * * * python TweetBot.py
```

### Features to be implemented in the future
- retweet tweets with specific keywords
- interaction with followers and other users

Follow me on [Twitter](https://twitter.com/ThePiTweetBot)
