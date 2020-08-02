import tweepy
from tweepy import OAuthHandler
import json
import wget
import os
import re
from storage import del_twitter_imgs

class twitter_class:

    def __init__(self):
 
        self.consumer_key = 'QyRWePO3smMVVsyxOmX7NHtXu'
        self.consumer_secret = 'l9dXMWeKgOIq4xFBQobNMh8dWw1pynj5m7Xv9tTMi7SCUP09O6'
        self.access_token = '1274586709334753280-0olVOuzzUAv6CN239mhveNi0ewZnHe'
        self.access_secret = 'ijpN8eqRAtseryIBNAfweyC52Uixuh4juSnz8gemJSoqD'

        self.usernames=["THacksters","Surya_Mohan_17"]

        self.media_files = list()
        self.tweet_list=list()
        self.img_list=list()
        self.profile_list=list()


    def twitter_data(self):
        path= "C:/Users/Surya Mohan/Desktop/test_rfrs/twitter_images/"
        count=1 
        @classmethod
        def parse(cls, api, raw):
            status = cls.first_parse(api, raw)
            setattr(status, 'json', json.dumps(raw))
            return status
         
        # Status() is the data model for a tweet
        tweepy.models.Status.first_parse = tweepy.models.Status.parse
        tweepy.models.Status.parse = parse
        # User() is the data model for a user profil
        tweepy.models.User.first_parse = tweepy.models.User.parse
        tweepy.models.User.parse = parse
        # You need to do it for all the models you need
         
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
         
        api = tweepy.API(auth)

        

        for username in self.usernames:

            tweets = api.user_timeline(screen_name=username,
                                       count=5, include_rts=False,
                                       exclude_replies=True)

            last_id = tweets[-1].id
             
            while (True):
                more_tweets = api.user_timeline(screen_name=username,
                                            count=5,
                                            include_rts=False,
                                                exclude_replies=True,
                                            max_id=last_id-1)
                
                
                  # There are no more tweets
                if (len(more_tweets) == 0):
                  break
                else:
                    last_id = more_tweets[-1].id-1
                    tweets = tweets + more_tweets

            
            for status in tweets:
                media = status.entities.get('media', [])
                text=status.text.encode("utf-8").decode()
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
                li=text.split(urls[0])
                twt=li[0]
                if(len(media) > 0):
                    self.media_files.append(media[0]['media_url'])
                    self.tweet_list.append(twt)
                    self.profile_list.append(username)

        if not len(os.listdir("twitter_images")) == 0:
            #print("empty")
            del_twitter_imgs()
        for media_file in self.media_files:
            wget.download(media_file,path+"img"+str(count)+".jpg")
            self.img_list.append(path+"img"+str(count)+".jpg")

            count=count+1
            #print(img_list)

    
#twitter_data()
'''t1=twitter_class()
t1.twitter_data()
print(t1.tweet_list)
print(t1.img_list)
print(t1.profile_list)'''
