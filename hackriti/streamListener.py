import tweepy
import boto3
import json

#client = boto3.client('firehose', region_name='us-east-1')
client = boto3.client('kinesis', region_name='us-east-1')

class MyStreamListener(tweepy.StreamListener):
    kinesisStreamName = ''
    partitionKey = ''
    def __init__(self,keyword,  api = None):

        super(MyStreamListener,self).__init__()
        print('-------constructor', keyword)
        self.kinesisStreamName = 'tweetstream'
        self.partitionKey = keyword
        #response = client.put_record(
        #    DeliveryStreamName='tweetstream',
        #    Record={
        #        'Data': json.dumps(keyword)
        #    }
        #)

    def on_status(self, status):
        self.putRecordInKinesisStream('Record')
        #f=open("guru999.txt", "a+")
        #f.write(status.text)
        #f.write('--------->')
        # print(status)
        #response = client.put_record(
        #    DeliveryStreamName='tweetstream',
        #    Record={
        #        'Data': json.dumps(status.text)
        #    }
        #)
        #print(response)
        response
        print('---------------->')

    def putRecordInKinesisStream(self, record, sequenceNumber):
        print('hey ', record)
        response = client.put_record(
            StreamName= 'tweets',
            Data=b'bytes',
            PartitionKey= self.partitionKey,
            SequenceNumberForOrdering='string'
        )
        return response


