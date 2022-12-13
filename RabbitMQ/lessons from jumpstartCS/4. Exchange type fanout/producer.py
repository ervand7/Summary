import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
message = 'Hello, i want to broadcast this message'
channel.basic_publish(exchange='pubsub', routing_key='', body=message)
print(f'sent message: {message}')
connection.close()
