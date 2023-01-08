import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='letterbox')
message = b'Hello, this is my first message'
channel.basic_publish(exchange='', routing_key='letterbox', body=message)
print(f'sent message: {message}')
connection.close()
