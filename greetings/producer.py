from kafka import KafkaProducer
from kafka.errors import KafkaError

class producer:
    def main():
        KAFKA_TOPIC = 'Topic5'
        producer = KafkaProducer(bootstrap_servers=['10.7.192.64:9092'], api_version=(0, 10, 1))
        #ip dinamico della macchina di dario
        producer.send(KAFKA_TOPIC, b'Hello, World!')
        producer.send(KAFKA_TOPIC, key=b'message-two', value=b'This is Kafka-Python')
        #producer.flush()
        #producer.close()