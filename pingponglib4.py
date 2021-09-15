# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time
import sys
from credentials import *

#enter corresponding information from your Twitter application management:
CONSUMER_KEY = 'vvoxphTOZwnGTqCMSeGVj591s' # consumer key
CONSUMER_SECRET = 'R9fPME92tkhOEUmhwwyG2Qor5TfWC1qDZMFN8AoSS2SH2XsDiw' # consumer secret key
ACCESS_TOKEN = '978777151683129347-b8BsNF3Ft5XS0xBcdXQF4JptcbCfpHE' #access token
ACCESS_SECRET = 'PwYGrbQX7pPzooiBemUyH624wHmjt7zWDm95MV1Uf4Yk1' # access token secret


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# access Twitter!
api = tweepy.API(auth)

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
