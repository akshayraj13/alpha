import tweepy
import boto3
import json

client = boto3.client('firehose', region_name='us-east-1')

class MyStreamListener(tweepy.StreamListener):

    def __init__(self,keyword,  api = None):

        super(MyStreamListener,self).__init__()
        print('-------constructor', keyword)

    def on_status(self, status):
        f=open("guru999.txt", "a+")
        f.write(status.text)
        f.write('--------->')
        # print(status)
        response = client.put_record(
            DeliveryStreamName='tweetstream',
            Record={
                'Data': json.dumps(status.text)
            }
        )
        #response = client.put_record(
        #   DeliveryStreamName='string',
        #  Record={
        #     'Data': 'bytes'
        # }
        #)
        print(response)
        print('---------------->')
