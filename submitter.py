import boto3
import pika
import traceback


def submit_data(key, data):
    try:
        s3 = boto3.resource('s3')
        s3.Bucket('eq-submissions').put_object(Key=key, Body=data)
    except Exception:
        print "You have a hole in your bucket, your bucket"


def on_message_received(ch, method, properties, body):
    print "Message Received"
    submit_data('messages.json', body)

def retrieve_data():
    try:
        credentials = pika.credentials.PlainCredentials('admin', 'admin')
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                                        host='david-rabbitmq1.eq.ons.digital',
                                        credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        channel.basic_consume(on_message_received,
                              queue='hello')

        print "Waiting for messages..."

        channel.start_consuming()

    except Exception:
        traceback.print_exc()
        print "connection error"

if __name__ == '__main__':
    retrieve_data()
