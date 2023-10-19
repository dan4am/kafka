import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
from time import sleep

def main():
    # consumer = KafkaConsumer('hello_world', bootstrap_servers=['localhost:9092'] )
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode("utf-8"),bootstrap_servers=['localhost:9092'])
    # producer.send('hello_world', {'key': 'value'})

    for e in range (1000):
        data = {'number' : e}
        print(data)
        producer.send("hello_world", data)
        sleep(3)

if __name__ == "__main__":
    main()