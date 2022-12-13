import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
message_analytics_only = 'This will be sent to analytics_only queue'
message_payments_only = 'This will be sent to payments_only queue'
message_both = 'This will be sent to both queue'

channel.basic_publish(
    exchange='routing', routing_key='analytics_only',
    body=message_analytics_only
)
channel.basic_publish(
    exchange='routing', routing_key='payments_only',
    body=message_payments_only
)
channel.basic_publish(
    exchange='routing', routing_key='both',
    body=message_both
)

print(f"""sent messages: 
{message_analytics_only}
{message_payments_only}
{message_both}
""")
connection.close()
