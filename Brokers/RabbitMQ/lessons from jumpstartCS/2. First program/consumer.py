import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties


def callback(
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes
):
    print(f'received new message: {body}')


connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='letterbox')
channel.basic_consume(
    queue='letterbox', auto_ack=True, on_message_callback=callback
)

print('Starting consuming')
channel.start_consuming()
