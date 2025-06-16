from confluent_kafka import Consumer
import json

consumer_conf = {
    'bootstrap.servers': 'BOOSTRAP-SERVER',  # Replace with your Kafka bootstrap server
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'CONFLUENT-API-KEY',  #
    'sasl.password': 'CONFLUENT-API-SECRET',  # Replace with your Confluent Cloud API key and secret
    'group.id': 'YOUR-GROUP-ID',  # Replace with your consumer group ID
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': True
}
consumer = Consumer(consumer_conf)
consumer.subscribe(['YOUR-TOPIC-NAME'])  # Replace with your Kafka topic name

print("Listening for weather data...\n")
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error:", msg.error())
        continue
    weather = json.loads(msg.value().decode('utf-8'))
    print(f"{weather['city']}, {weather['country']} - {weather['description'].capitalize()} at {weather['temperature']}°C")
