from tweepy import StreamListener
from tweepy import Stream
import tweepy
import json

consumer_key= 'oXEsPKoCY80yfEgMqNkgbrWOh'
consumer_secret= 'qLjVnNexnKZ6ISSwUVzd9nP0l8u30EUNwi11CwWhESlBKictCf'
access_token= '850161275539771392-kfUjQUdg6TFxAUncaLeKmKwrw4gdwAL'
access_token_secret= '5OA3Dcafb5DPPpBJmHDLtN65COpUnNuAzdN92s6CpPKHQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class StdOutListener(StreamListener):

  def on_data(self, data):
    tweet_data = json.loads(data)
    print (tweet_data)
    print ('++++++++++++++++++++++++++++++++++++++++++++++++')
    print (tweet_data['text'])
    print (tweet_data['entities']['media'][0]['media_url_https'])

  def on_error(self, status):
    print (status)

if __name__ == '__main__':
  screen_user = input("Please enter the twitter user data you want collect ")
  user = api.get_user(screen_user)
  listener = StdOutListener()
  twitterStream = Stream(auth, listener)
  twitterStream.filter(follow=[str(user.id)])