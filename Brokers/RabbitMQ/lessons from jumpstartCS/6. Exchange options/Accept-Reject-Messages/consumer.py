import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.exchange_type import ExchangeType
from pika.spec import Basic, BasicProperties


def callback(
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes
):
    # delivery_tag - просто счетчик сообщений
    if method.delivery_tag % 5 == 0:
        ch.basic_nack(
            delivery_tag=method.delivery_tag, requeue=False, multiple=True
        )
    print(f'Received new message: {method.delivery_tag}')


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(
    exchange='accept_reject_exchange',
    exchange_type=ExchangeType.fanout
)
channel.queue_declare(queue='letterbox')
channel.queue_bind('letterbox', 'accept_reject_exchange')
channel.basic_consume(queue='letterbox', on_message_callback=callback)

print('Starting Consuming')
channel.start_consuming()
