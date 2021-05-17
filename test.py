from research_twitterapi import ResearchTwitterApi
from send_twitterapi import SendTwitterApi
import config

#API_KEYS
# testuser
test_api_keys = {
    'consumer_api_key':config.TEST_CONSUMER_API_KEY
    ,'consumer_api_secret_key':config.TEST_CONSUMER_API_SECRET_KEY
    ,'token_access_key':config.TEST_TOKEN_ACCESS_KEY
    ,'token_access_secret_key':config.TEST_TOKEN_ACCESS_SECRET_KEY
    ,'user_name':config.TEST_USER_NAME
}

#TestAPI 
research_twitter = ResearchTwitterApi(**test_api_keys)
send_twitter = SendTwitterApi(**test_api_keys)

#'/mnt/hdd1/Data/git_train/autotwitter/res/image/test.jpeg'
research_twitter.acquire_follows()

