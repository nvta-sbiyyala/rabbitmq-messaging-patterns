# consumer.py
import pika


def callback(ch, method, properties, body):
    print(f"Consumer received: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge the message


def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='demo_queue', durable=True)

    print("Consumer is waiting for messages...")
    channel.basic_consume(queue='demo_queue', on_message_callback=callback)

    channel.start_consuming()


if __name__ == "__main__":
    consume()
