import boto3
import pika
import traceback


def submit_data(ch, method, properties, body):
    try:
        s3 = boto3.resource('s3')
        s3.Bucket('eq-submissions').put_object(Key=body, Body=body)
    except Exception:
        print "You have a hole in your bucket, your bucket"



def create_data(body):
    credentials = pika.credentials.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='david-rabbitmq1.eq.ons.digital', credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='eq-submissions')
    channel.basic_publish(exchange='', routing_key='eq-submissions', body=body)
    connection.close()

def retrieve_data():
    try:
        credentials = pika.credentials.PlainCredentials('admin', 'admin')
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                                        host='david-rabbitmq1.eq.ons.digital',
                                        credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue='eq-submissions')
        channel.basic_consume(submit_data, queue='eq-submissions')
        channel.start_consuming()


    except Exception:
        traceback.print_exc()
        print "connection error"

if __name__ == '__main__':
    retrieve_data()