import random
import time

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties


def callback(
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes
):
    processing_time = random.randint(1, 6)
    print(f'received: {body}, will take {processing_time} to process')
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('Finished processing the message')


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='letterbox')
channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue='letterbox', on_message_callback=callback
)

print('Starting consuming')
channel.start_consuming()
