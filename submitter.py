import boto3
import pika
import traceback
import settings


def submit_data(ch, method, properties, body):
    try:
        s3 = boto3.resource('s3')
        s3.Bucket('eq-submissions').put_object(Key=body, Body=body)
    except Exception:
        print "You have a hole in your bucket, your bucket"


def create_data(body):
    connection_parameters = pika.URLParameters(settings.EQ_RABBITMQ_URL)
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue=settings.EQ_RABBITMQ_QUEUE_NAME)
    channel.basic_publish(exchange='',
                          routing_key=settings.EQ_RABBITMQ_QUEUE_NAME,
                          body=body)
    connection.close()


def retrieve_data():
    try:
        connection_parameters = pika.URLParameters(settings.EQ_RABBITMQ_URL)
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()
        channel.queue_declare(queue=settings.EQ_RABBITMQ_QUEUE_NAME)

        channel.basic_consume(submit_data,
                              queue=settings.EQ_RABBITMQ_QUEUE_NAME)

        channel.start_consuming()

    except Exception:
        traceback.print_exc()
        print "connection error"
