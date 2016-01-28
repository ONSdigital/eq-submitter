# Setup the connection string: the 2%F refers to the '/' virtual host
import os

EQ_RABBITMQ_URL = os.getenv('EQ_RABBITMQ_URL')
EQ_RABBITMQ_QUEUE_NAME = os.getenv('EQ_RABBITMQ_QUEUE_NAME')
EQ_SUBMISSIONS_BUCKET_NAME = os.getenv('EQ_SUBMISSIONS_BUCKET_NAME')
