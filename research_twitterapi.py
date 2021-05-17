import tweepy
from requests_oauthlib import OAuth1Session

from twitterapi import TwitterApi
import json
import datetime, time, sys

class ResearchTwitterApi(TwitterApi):
    def __init__(self, consumer_api_key, consumer_api_secret_key, token_access_key, token_access_secret_key, user_name):
        super().__init__(consumer_api_key, consumer_api_secret_key, token_access_key, token_access_secret_key, user_name)
        self.session = OAuth1Session(consumer_api_key, consumer_api_secret_key, token_access_key, token_access_secret_key)

    def acquire_timeline(self, line_count):      
        #Timeline取得
        for status in self.api.home_timeline(count=line_count):
            #見映えのため区切る
            print('-------------------------------------------')
            #ユーザ名表示
            print('name:' + status.user.name)
            #内容表示
            print(status.text)

    def acquire_followids(self):
        #FollowしているID取得
        following_ids = self.api.friends_ids(self.user_name)
        print(len(following_ids))

    def acquire_follows(self):
        # follows = self.api.friends(screen_name=self.user_name)
        # print(follows)

        #friendslist
        # url = "https://api.twitter.com/1.1/friends/list.json?screen_name=" + self.user_name
        # cursor = -1
        # while cursor != 0:
        #     res = self.session.get(url, params = {'count':40, 'cursor':cursor})
        #     if res.status_code != 200:
        #         print ("Twitter API Error: %d" % res.status_code)
        #         sys.exit(1)

        #     print ('アクセス可能回数 %s' % res.headers['X-Rate-Limit-Remaining'])
        #     print ('リセット時間 %s' % res.headers['X-Rate-Limit-Reset'])
        #     sec = int(res.headers['X-Rate-Limit-Reset'])\
        #             - time.mktime(datetime.datetime.now().timetuple())
        #     print ('リセット時間 （残り秒数に換算） %s' % sec)

        #     res_text = json.loads(res.text)
        #     for user in res_text['users']:
        #         # print (tweet['created_at'])
        #         if user['following']:
        #             print (user['name'])

        #     cursor = res_text['next_cursor']

        #follows
        friends_url = "https://api.twitter.com/1.1/friends/ids.json"
        followers_url = "https://api.twitter.com/1.1/followers/ids.json"
        friends_res = self.session.get(friends_url, params = {'screen_name':self.user_name})
        followers_res = self.session.get(followers_url, params = {'screen_name':self.user_name})
        res_list = [friends_res, followers_res]

        ids_set = ()
        ids_list = []
        for i, res in enumerate(res_list):
            if res.status_code != 200:
                print ("Twitter API Error: %d" % res.status_code)
                sys.exit(1)

            print ('アクセス可能回数 %s' % res.headers['X-Rate-Limit-Remaining'])
            print ('リセット時間 %s' % res.headers['X-Rate-Limit-Reset'])
            sec = int(res.headers['X-Rate-Limit-Reset'])\
                    - time.mktime(datetime.datetime.now().timetuple())
            print ('リセット時間 （残り秒数に換算） %s' % sec)

            res_text = json.loads(res.text)
            ids_set = set(res_text['ids'])
            ids_list.append(ids_set)

        fllowers = ids_list[0] - ids_list[1]

        print(len(fllowers))
        nofollow_list = self.api.lookup_users(user_ids=fllowers)
        for nofollow in nofollow_list:
            print(nofollow.name)
        

