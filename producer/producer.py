''' Script that wrties randomly generated IoT sensor data to a Kafka topic '''

import random
import time
import json
from kafka import KafkaProducer
from datetime import datetime

# initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda value: json.dumps(value).encode('utf-8')
)

def generate_data():
    while True:
        data = {
            'temperature': round(random.uniform(-10, 40)), # -10 to 40 deg C
            'humidity': round(random.uniform(0, 100)), # 0 to 100 %
            'air_pressure': round(random.uniform(950, 1050)), # 950 to 1050 hectoPascals
            'timestamp': datetime.now().isoformat() # YYYY-MM-DDTHH:MM:SS format
        }
        # send data to topic
        producer.send('raw_iot_data', data)
        print(f"produced data: {data}")
        # wait 2 seconds before sending next data message
        time.sleep(2)


if __name__ == "__main__":
    try:
        generate_data()
    except KeyboardInterrupt:
        print("Producer stopped.")
    finally:
        producer.close()
