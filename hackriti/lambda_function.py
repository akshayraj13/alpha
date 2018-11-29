import json
import tweepy
from streamlistener.py import MyStreamListener


def lambda_handler(event, context):

    auth = tweepy.OAuthHandler('o2ipQeWmf1nRnmo9KuL54kYnr', 'hJjygIOjoS34Dv6n6DBYSzOSVHSHdey3AsaUcnpBT1A56GL9px')
    auth.set_access_token('1067670046900514816-7U45hCQmSethnnL2ApCIu4Dej1Lkh4', 'GK73yynnkFgBh4qd9SONpnNswFbQ70DmTLLeYQLYDOQNX')
    api = tweepy.API(auth)
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['Donald Trump'])
    return {
        'statusCode': 200,
        'body': json.dumps("hello world")
    }