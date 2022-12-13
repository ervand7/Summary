import pika


def callback(ch, method, properties, body):
    print(f"Received Request: {properties.correlation_id} with body: {body}")
    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        body=f'Hey its your reply to {properties.correlation_id}'
    )


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='request-queue')
channel.basic_consume(
    queue='request-queue',
    auto_ack=True,
    on_message_callback=callback
)

print("Starting Server")
channel.start_consuming()
