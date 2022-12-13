import json
import uuid

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

order = {
    'id': str(uuid.uuid4()),
    'user_email': 'john.doe@example.com',
    'product': 'Leather Jacket',
    'quantity': 1
}

channel.basic_publish(
    exchange='order',
    routing_key='order.notify',
    body=json.dumps({'user_email': order['user_email']})
)
print(' [x] Sent notify message')

channel.basic_publish(
    exchange='order',
    routing_key='order.report',
    body=json.dumps(order)
)
print(' [x] Sent report message')

connection.close()
