import sys
import tweepy
import json

key = ''
secret = ''
access_key = ''
access_secret = ''
save_path = 'tweets.json'
Q = sys.argv[1:]
output = open(save_path, 'w') 
class Listener(tweepy.StreamListener):
  def on_status(self, status):
    t = status.text
    print t
    output.write(json.dumps(t))
    output.flush()
    
  def on_error(self, status):
    print status

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_key, access_secret)

l = Listener()
streamer = tweepy.Stream(auth, l)
streamer.filter(track = Q)

