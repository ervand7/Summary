import pika
from pika.exchange_type import ExchangeType


def callback(ch, method, properties, body):
    print(f'consumer2: received new message: {body}')


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
queue = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)
channel.basic_consume(
    queue=queue.method.queue, auto_ack=True, on_message_callback=callback
)

print('Starting consuming')
channel.start_consuming()
