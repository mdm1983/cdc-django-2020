from kafka import KafkaProducer
from kafka.errors import KafkaError

class producer:
    def main():
        producer = KafkaProducer(bootstrap_servers=['10.7.10.156:9092'], api_version=(0, 10, 1))
        print('producer created')
        producer.send('Topic1', b'Hello, World!')
        print('producer send 1')
        producer.send('Topic2', key=b'message-two', value=b'This is Kafka-Python')
        print('producer send 2')