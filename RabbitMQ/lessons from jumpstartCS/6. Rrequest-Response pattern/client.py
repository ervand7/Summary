import uuid

import pika


def callback(ch, method, properties, body):
    print(f"reply received: {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
reply_queue = channel.queue_declare(queue='', exclusive=True)
channel.basic_consume(
    queue=reply_queue.method.queue,
    auto_ack=True,
    on_message_callback=callback
)

channel.queue_declare(queue='request-queue')
request_id = str(uuid.uuid4())
print(f"Sending Request: {request_id}")

channel.basic_publish(
    exchange='',
    routing_key='request-queue',
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=request_id),
    body='Can I request a reply?'
)

print("Starting Client")
channel.start_consuming()
