import tweepy

consumer_key= 'oXEsPKoCY80yfEgMqNkgbrWOh'
consumer_secret= 'qLjVnNexnKZ6ISSwUVzd9nP0l8u30EUNwi11CwWhESlBKictCf'
access_token= '850161275539771392-kfUjQUdg6TFxAUncaLeKmKwrw4gdwAL'
access_token_secret= '5OA3Dcafb5DPPpBJmHDLtN65COpUnNuAzdN92s6CpPKHQ'

if __name__ == '__main__':
    user = input("Please enter the twitter user data you want collect ")

    # Create authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    
    print ("Getting statistics for", user)

    # Get information about the user
    data = api.get_user(user)
    
    print ('Followers: ' + str(data.followers_count))
    print ('Tweets: ' + str(data.statuses_count))
    print ('Favouries: ' + str(data.favourites_count))
    print ('Friends: ' + str(data.friends_count))
    print ('Appears on ' + str(data.listed_count) + ' lists')
    print ('------------------------------------------------')
    tweets = api.user_timeline(screen_name = user,count=200)
    for tweet in tweets:
        print (tweet.text)
        print ('-------------------')
