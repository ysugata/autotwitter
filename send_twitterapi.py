import tweepy
from twitterapi import TwitterApi

class SendTwitterApi(TwitterApi):
    def __init__(self, consumer_api_key, consumer_api_secret_key, token_access_key, token_access_secret_key, user_name):
        super().__init__(consumer_api_key, consumer_api_secret_key, token_access_key, token_access_secret_key, user_name)
    
    def tweet_content(self, tweet_content):
        #Tweet 
        self.api.update_status(status=tweet_content)

    def tweet_image_content(self, image_path, content):
        #Tweet 画像つき
        self.api.update_with_media(filename=image_path,status=content)

