import boto3
import pika
import traceback
import settings

class S3Submitter(object):

    def submit_data(self, key, message):
        try:
            s3 = boto3.resource('s3')
            s3.Bucket(settings.EQ_SUBMISSIONS_BUCKET_NAME).put_object(Key=message, Body=message)
            return True
        except Exception:
            traceback.print_exc()
            print "You have a hole in your bucket, your bucket"
            return False
