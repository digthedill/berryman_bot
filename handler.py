import base64
from pprint import pprint
import os
import random
import string
import tweepy
import requests

content_path = "./content/sonnets.txt"
content_path = os.path.join(os.path.dirname(__file__), content_path)

twitter_base_url = "https://api.twitter.com/1.1"


auth = tweepy.OAuth1UserHandler(
    os.environ["CONSUMER_KEY"],
    os.environ["CONSUMER_KEY_SECRET"],
    os.environ["ACCESS_TOKEN"],
    os.environ["ACCESS_TOKEN_SECRET"]
)
api = tweepy.API(auth)


def run(event, context):
    print("Berryman bot started")

    payload = ""

    # parse content/sonnet.txt
    with open(content_path, "r") as f:
        lines = f.readlines()

        #  remove newline characters
        lines = [line.strip() for line in lines]
        # remove lines starting with []
        lines = [line for line in lines if not line.startswith("[")]

        random_index = random.randint(0, len(lines)-1)

        try:
            for i, line in enumerate(lines):
                if i == random_index:
                    tweet = line.capitalize()
                    # if last character is not punctuation

                    if len(tweet) == 0:
                        random_index = random.randint(0, len(lines)-1)

                    if tweet[-1] in string.punctuation:
                        tweet = tweet[:-1]
                    else:
                        tweet = tweet + "\r\n " + lines[i + 1].capitalize()
                        print(len(tweet))

                    # maybe some logic  for two lines of text?
                    payload += tweet
        except Exception as e:
            print(e)
            payload["status"] = "Error: " + str(e)

    # check if tweet exists

    # send tweet

    try:
        api.update_status(payload)

    except Exception as e:
        print(e)
        payload["status"] = "Error: " + str(e)

    return payload
