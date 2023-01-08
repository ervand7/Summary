import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(
    exchange='alt_exchange', exchange_type=ExchangeType.fanout)

channel.exchange_declare(
    exchange='main_exchange', exchange_type=ExchangeType.direct,
    arguments={'alternate-exchange': 'alt_exchange'}
)

message = 'Hello this is my first message'
channel.basic_publish(
    exchange='main_exchange', routing_key='test', body=message
)

print(f'sent message: {message}')
connection.close()
