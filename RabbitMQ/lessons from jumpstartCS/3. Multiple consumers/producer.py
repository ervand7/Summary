import random
import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='letterbox')

message_id = 1
while True:
    message = f'Sending messageID: {message_id}'
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    print(f'sent message: {message}')
    time.sleep(random.randint(1, 4))
    message_id += 1
