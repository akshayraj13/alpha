import tweepy

auth = tweepy.OAuthHandler('o2ipQeWmf1nRnmo9KuL54kYnr', 'hJjygIOjoS34Dv6n6DBYSzOSVHSHdey3AsaUcnpBT1A56GL9px')
auth.set_access_token('1067670046900514816-7U45hCQmSethnnL2ApCIu4Dej1Lkh4', 'GK73yynnkFgBh4qd9SONpnNswFbQ70DmTLLeYQLYDOQNX')

api = tweepy.API(auth)
user = api.get_user('twitter')
print(user.screen_name)
print(user.followers_count)

public_tweets = api.home_timeline()
print('akshay')

print('raj')
for tweet in public_tweets:
    print(tweet.text)