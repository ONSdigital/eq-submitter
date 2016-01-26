import boto3
import pika


def submit_data(key, data):
     try:
          s3 = boto3.resource('s3')
          s3.Bucket('eq-submissions').put_object(Key=key, Body=data)
     except Exception:
          print "You have a hole in your bucket, your bucket"


def retrieve_data():
     try:
          credentials = pika.credentials.PlainCredentials('admin', 'admin')
          connection = pika.BlockingConnection(pika.ConnectionParameters
                                          (host='david-rabbitmq1.eq.ons.digital', credentials=credentials))
          channel = connection.channel()

          for body in channel.consume('hello'):
               submit_data('json', body)
     except Exception:
          print "connection error"