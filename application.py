from submission_consumer import SubmissionConsumer
from submitters import S3Submitter
import settings

def message_received(message):
    print('Received: %s', message)
    return submitter.submit_data(None, message)

if __name__ == '__main__':
    print "Consuming messages from {} on {}".format(settings.EQ_RABBITMQ_QUEUE_NAME, settings.EQ_RABBITMQ_URL)
    consumer = SubmissionConsumer(settings.EQ_RABBITMQ_URL, settings.EQ_RABBITMQ_QUEUE_NAME)
    submitter = S3Submitter()
    consumer.message_received=message_received
    consumer.run()
