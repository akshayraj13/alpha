import tweepy
import simplejson as json
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    count = 0
    def __init__(self, api = None):
        super(MyStreamListener,self).__init__()
        self.count = 0

    def on_status(self, status):
        if self.count == 0 :
            self.count += 1
            json.dumps(status._json)
            f=open("guruG.txt", "a+")
            f.write(json.dumps(status._json))
            f.close()
            print(status)

            print('---------------->')


auth = tweepy.OAuthHandler('o2ipQeWmf1nRnmo9KuL54kYnr', 'hJjygIOjoS34Dv6n6DBYSzOSVHSHdey3AsaUcnpBT1A56GL9px')
auth.set_access_token('1067670046900514816-7U45hCQmSethnnL2ApCIu4Dej1Lkh4', 'GK73yynnkFgBh4qd9SONpnNswFbQ70DmTLLeYQLYDOQNX')

api = tweepy.API(auth)
myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['brexit'])
