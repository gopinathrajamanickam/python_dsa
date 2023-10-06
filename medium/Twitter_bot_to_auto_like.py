"""
Creating a Twitter bot  to auto like  all the tweets with a specific
hastag

"""

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    consumer_key="YOUR_CONSUMER_KEY",
    consumer_secret="YOUR_CONSUME_SECRET",
    access_token="YOUR_ACCESS_TOKEN",
    access_token_secret="YOUR_ACCESS_TOKEN"
)
api = tweepy.API(auth)

# Auto-like tweets with hatag #PythonRocks

for tweet in tweepy.Cursor(api.search,q="#Pythonocks", lang="en").items(5):
    try:
        print(f"Liking tweet by @{tweet.user.screen_name}")
        tweet.favorite()
    except tweepy.TweepError as e:
        print(e.reason)






