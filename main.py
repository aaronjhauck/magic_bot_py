import schedule
import time
import os
from dotenv import load_dotenv
from twython import Twython
from sentences import get_sentence

load_dotenv()
my_tweet = get_sentence()

twitter = Twython(
    os.getenv('consumer_key'),
    os.getenv('consumer_secret'),
    os.getenv('access_token'),
    os.getenv('access_token_secret')
)

def job():
    twitter.update_status(status=my_tweet)
    print(f"Tweeted:\n{my_tweet}")


schedule.every().sunday.at("13:00").do(job)
schedule.every().tuesday.at("13:00").do(job)
schedule.every().thursday.at("13:00").do(job)
schedule.every().friday.at("13:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
