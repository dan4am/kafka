import os
from kafka import KafkaProducer
import json

class ADT():
    def __init__(self, properties:dict, name:str ):
        self.properties = properties
        self.name = name
        self.producer = None
        self.topic_out =""
        self.topic_in =""
        pass
    def start(self):
        commande1 = "C:\kafka_2.12-3.6.0\\bin\windows\kafka-topics.bat --create --topic "
        topic = self.name + "_out"
        self.topic_out = topic
        commande2 = " --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1"
        commande = commande1+topic+commande2
        print(commande)
        retour_commande = os.popen(commande).read()
        # print(retour_commande)
        self.producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode("utf-8"), bootstrap_servers=['localhost:9092'] )

    def publish(self, message):
        self.producer.send(self.topic_out,message)

    def set(self, prop, new_value):
        old = self.properties[prop]
        self.properties[prop] = new_value
        print("change = "+ str(new_value) + " , from = "+ str(old))
        print(self.properties)
        self.publish({"change" : "size = "+str(new_value)+" from "+ str(old)})


def main():
   test_adt = ADT({'size':10}, "test_adt_3")
   test_adt.start()
   test_adt.set("size", 25)


if __name__ == "__main__":
    main()