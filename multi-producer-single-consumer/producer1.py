# producer1.py
import pika
import time


def produce():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    for i in range(10000):
        message = f"Message from Producer 1 - {i}"
        channel.basic_publish(
            exchange='demo_exchange',
            routing_key='demo_routing_key',
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),  # Persistent messages
        )
        print(f"Producer 1 sent: {message}")
        time.sleep(1)

    connection.close()


if __name__ == "__main__":
    produce()
