import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.exchange_type import ExchangeType
from pika.spec import Basic, BasicProperties


def alt_callback(
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes
):
    print(f'Alt - received new message: {body}')


def main_callback(
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes
):
    print(f'Main - received new message: {body}')


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(
    exchange='alt_exchange',
    exchange_type=ExchangeType.fanout
)
channel.exchange_declare(
    exchange='main_exchange',
    exchange_type=ExchangeType.direct,
    arguments={'alternate-exchange': 'alt_exchange'}
)
channel.queue_declare(queue='alt_exchange_queue')
channel.queue_bind('alt_exchange_queue', 'alt_exchange')
channel.basic_consume(
    queue='alt_exchange_queue', on_message_callback=alt_callback
)

channel.queue_declare(queue='main_exchange_queue')
channel.queue_bind('main_exchange_queue', 'main_exchange', 'test')
channel.basic_consume(
    queue='main_exchange_queue', on_message_callback=main_callback
)

print('Starting Consuming')
channel.start_consuming()
