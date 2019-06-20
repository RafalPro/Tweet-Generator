from django.db import models
from twitter import *
import re
import markovify
from django.shortcuts import redirect

# Create your models here.

class TwitterUser:
    allUsers = {}
    
    def __init__(self, name):
        self.name = name
        self.get_tweets(name)
        TwitterUser.allUsers[name] = self
    
    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name


    def get_tweets(self, username):
        #authenticate my twitter and make an api
        consumer_key="DG2G7kfyrVAPsdmvJR50G5b10"
        consumer_secret="ipq1UzmDIptgpU78s0Zc00dc6dvsv4SMiJxSEoM7onm4TYJ20K"
        access_token_key="2178855848-OKbdpAjKQRMlIfGXuiqxCn5t7SjMtPRgIVkkFo0"
        access_token_secret="2IP23yWIImu4j02w8h19J6gbsljQPvxjYa62vPODyaSbI"
        t = Twitter(auth=OAuth(access_token_key, access_token_secret, consumer_key, consumer_secret))

        #gets the first 800 tweets of Donald Trump
        handle = username.replace('@', '')
        trump_statuses = t.statuses.user_timeline(screen_name=handle, include_rts=False, count=800, tweet_mode='extended')

        #compile all Donald Trump's tweets into a single string and print the rest
        text = ""
        for status in trump_statuses:
            subject = status['full_text']
            final = re.sub(r"http\S+", "", subject)
            text += final
            text += " \n"
        self.body = text

    def generate_tweet(self):
        text_model = markovify.NewlineText(self.body)
        return(text_model.make_sentence(tries=10000))