# National Gallery Art Twitter Bot
This bot generates daily tweets at [@natgallerysgbot](https://twitter.com/natgallerysgbot), detailing artworks from the National Gallery Singapore's (beautiful place!) [collection](https://collections.nationalgallery.sg/#/).

## Built with
- [Tweepy](https://www.tweepy.org/) library
- [Heroku](https://www.heroku.com/) hosting

## Building locally
1. Install Python 3.6 or newer
2. Clone the repo
3. `cd natgallerysg_twitterbot`
4. Create a virtual environment (optional)
5. Run `pip install -r requirements.txt`
6. Create a new twitter account
7. Obtain developer keys and update `local_settings.py`
8. Run `python bot.py`

This will post a tweet to your Twitter account.

## References
- Inspired by existing [Museum Twitter Bots](https://backspace.com/is/in/the/house/work/pg/twitter_bots.html)
- https://github.com/dariusk/museumbot (and many other Twitter bot examples)
- https://hackernoon.com/deploying-twitter-bot-to-heroku-6b143uaj
