# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time
import sys
from credentials import *

#enter the corresponding information from your Twitter application management:
CONSUMER_KEY = 'vvoxphTOZwnGTqCMSeGVj591s' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'R9fPME92tkhOEUmhwwyG2Qor5TfWC1qDZMFN8AoSS2SH2XsDiw' #keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '978777151683129347-b8BsNF3Ft5XS0xBcdXQF4JptcbCfpHE' #keep the quotes, replace this with your access token
ACCESS_SECRET = 'PwYGrbQX7pPzooiBemUyH624wHmjt7zWDm95MV1Uf4Yk1' #keep the quotes, replace this with your access token secret


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# access Twitter!
api = tweepy.API(auth)
"""
# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search, q='reading',since='2017-11-25',lang='fr').items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

         # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        time.sleep(7200)
        #sleep(3600) this function takes in seconds as its parameter

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
"""
# open our content file and read each line
filename=open('q.txt')
f=filename.readlines()
filename.close()

# for each line in our contents file, lets tweet that line out except when we hit a error

def update():
    for line in f:
        try:
            while True:
                api.update_status(line)
                #api.update_status(tweet)
                print("tweeted")
                time.sleep(1800)
                
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(5) #Tweet every 2 minutes
            print("All done")
        except StopIteration:
            break
   
update()
