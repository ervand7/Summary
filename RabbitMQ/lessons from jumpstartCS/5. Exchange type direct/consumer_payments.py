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
    print(f'Payments - received new message: {body}')


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
queue = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(
    exchange='routing', queue=queue.method.queue, routing_key='payments_only'
)
channel.queue_bind(
    exchange='routing', queue=queue.method.queue, routing_key='both'
)
channel.basic_consume(
    queue=queue.method.queue, auto_ack=True, on_message_callback=callback
)
# queue.method.queue будет представлен как amq.gen-hxD_H-U5LAIcPhTkDgsf5A
print('Payments Starting Consuming')
channel.start_consuming()
