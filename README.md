# eq-submitter

Requires the following environment variables:

```
EQ_RABBITMQ_URL               # The URL to the RabbitMQ Load Balancer
EQ_RABBITMQ_QUEUE_NAME        # The name of the queue
EQ_SUBMISSIONS_BUCKET_NAME    # The name of the S3 Bucket

AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY
```

## Installing in production

```
sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install supervisor
sudo apt-get install unzip
```

```
wget https://github.com/ONSDigital/eq-submitter/archive/eq-16-submitter-foundation.zip
mv eq-submitter-master eq-submitter
cd eq-submitter
sudo pip install -r requirements.txt
```

Edit the supervisor.conf file and provide the appropriate environment variables
then copy the file into place.

```
cp supervisor.conf /etc/supervisor/conf.d/submitter.conf
```

Once copied, restart the `supervisor` service

```
sudo service supervisor restart
```
