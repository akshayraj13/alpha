import tweepy

# override tweepy.StreamListener to add logic to on_status


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        f=open("guru99.txt", "a+")
        f.write(status.text)
        print(status.text)
