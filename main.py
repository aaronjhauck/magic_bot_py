import os
import time
import pycron
from twython import Twython
from datetime import datetime
from dotenv import load_dotenv
from sentences import get_sentence

load_dotenv()

twitter = Twython(
    os.getenv('consumer_key'),
    os.getenv('consumer_secret'),
    os.getenv('access_token'),
    os.getenv('access_token_secret')
)

def log_message(message):
    now = datetime.now()
    dt_string = now.strftime("[%d-%m-%Y %H:%M:%S]")
    print(f"{dt_string} : {message}")

def send_tweet(tweet):
    twitter.update_status(status=tweet)

while True:
    if pycron.is_now('0 13 * * 0,2,4,5'):
        my_tweet = get_sentence()
        log_message("Begining tweet function...")
        log_message(f"Sentence: {my_tweet}")
        log_message("Attepting to tweet...")
        try:
            send_tweet(my_tweet)
            log_message("Successfully Tweeted!")
        except Exception as ex:
            log_message("Unable to send tweet.")
            log_message(f"{ex}")
        time.sleep(60)
    else:
        time.sleep(15)
