# 3 Nov
- python 13 in a virtual environment called .producer-env
- to check which python is running: import sys; print(sys.executable)
- kafka-python import was producing error so had to install from a git branch: pip install --break-system-packages git+https://github.com/dpkp/kafka-python.git
- kafka topic to which producer writes is called 'raw_iot_data'

# run insstructions (3 Nov)
- start zookeeper and kafka server in WSL
- run producer.py to write data every 2 secs to 'raw_iot_data' topic
- check data using consumer.py script or directly using kafka console consumer

## running kafka
- since kafka is running on WSL and my script on windows, had to modify the listeners in config/server.properties in the kafka dir. set listeners=PLAINTEXT://0.0.0.0:9092
and set advertised.listeners=PLAINTEXT://<WSL_IP_Address>:9092 (You can find your WSL IP address by running ip addr in your WSL terminal and looking for the eth0 interface. Alternatively, you can use localhost if you're just testing locally.)

## command shortcuts
### kafka
- start zookeeper: bin/zookeeper-server-start.sh config/zookeeper.properties
- start kafka server: bin/kafka-server-start.sh config/server.properties
- create topic: bin/kafka-topics.sh --create --topic my_topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
- verify topic creation: bin/kafka-topics.sh --list --bootstrap-server localhost:9092
- start producer: bin/kafka-console-producer.sh --topic my_topic --bootstrap-server localhost:9092
- start consumer: bin/kafka-console-consumer.sh --topic my_topic --from-beginning --bootstrap-server localhost:9092
- delete topic: ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic my-topic
- we can also selectively delete records: ./bin/kafka-delete-records.sh --bootstrap-server localhost:9092 --offset-json-file delete-records.json
- change message retention rate: kafka-configs.sh --alter --entity-type topics --entity-name test-topic --add-config retention.ms=60000

### general
