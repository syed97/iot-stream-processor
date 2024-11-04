'''test file to see data being generated'''

from kafka import KafkaConsumer
import json

# Initialize the Kafka consumer
consumer = KafkaConsumer(
    'raw_iot_data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    group_id='my-group'
)

for message in consumer:
    print(f"Consumed: {message.value}")
