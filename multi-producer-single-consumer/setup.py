# setup.py
import pika


def setup_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare an exchange
    channel.exchange_declare(exchange='demo_exchange', exchange_type='direct', durable=True)

    # Declare a queue
    channel.queue_declare(queue='demo_queue', durable=True)

    # Bind the queue to the exchange
    channel.queue_bind(exchange='demo_exchange', queue='demo_queue', routing_key='demo_routing_key')

    print("RabbitMQ setup complete!")
    connection.close()


if __name__ == "__main__":
    setup_rabbitmq()
