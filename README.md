# @ThePiTweetBot

### Features

- dynamic randomised tweets retrieved from a text file every hour
- tweets CPU temperature at the beginning of every third hour
- tweet .jpg files
- local 140-characters message limit
- automatic script running using crontab:
```
sudo crontab -e

*/60 * * * * python TweetBot.py
0 */3 * * * python TweetBotCPU.py
```

### Features to be implemented in the future
- write to a log each time script is ran to keep track of tweets sent
- retweet tweets with specific keywords
- interaction with followers and other users

Follow me on [Twitter](https://twitter.com/ThePiTweetBot)
