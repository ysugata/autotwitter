import tweepy

class TwitterApi(object):
    def __init__(self, consumer_api_key, consumer_api_secret_key, token_access_key, token_access_secret_key, user_name):
        auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
        auth.set_access_token(token_access_key,token_access_secret_key)

        self.api = tweepy.API(auth,
                        retry_count=5,
                        retry_delay=10,
                        retry_errors=set({401, 404, 500, 503}),
                        wait_on_rate_limit=True)
        self.user_name = user_name

