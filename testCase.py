import json
import random
import threading

import paho.mqtt.client as mqtt
import time

from config import IP, TOPIC_AK, ACTION, END_CONNECT, START_CONNECT, BUTTON, PORT, DEBUG, TOPIC_KA


class TestCase:
    def __init__(self):
        self.id = random.randint(0,10)

    def testCase1(self):
        self.mqttClient = mqtt.Client()
        self.mqttClient.on_connect = self.on_connect
        self.mqttClient.on_disconnect = self.on_disconnect
        self.mqttClient.on_message = self.on_message

        # self.mqttClient.loop_start()
        self.mqttClient.connect(IP, port = PORT)

        self.mqttClient.subscribe(TOPIC_KA)
        self.mqttClient.loop_forever()

        # time.sleep(3)
        # self.publishTestMessage()

        # time.sleep(15)

        # self.mqttClient.publish(TOPIC_AK, json.dumps({"clientId" : self.id,"purpose": END_CONNECT}))
        # self.mqttClient.disconnect()

    def mainLoop(self):
        self.publishTestMessage()

        time.sleep(15)
        self.mqttClient.publish(TOPIC_AK, json.dumps({"clientId" : self.id,"purpose": END_CONNECT}))
        self.mqttClient.disconnect()

    def publishTestMessage(self):
        self.mqttClient.publish(TOPIC_AK, json.dumps({"clientId" : self.id,"purpose": ACTION, "virtualKey" : "0", "clickType" : BUTTON}))

    def on_connect(self, client, userdata, flags, rc):
        # client.publish(TOPIC_AK, json.dumps({"clientId" : 0,"purpose": START_CONNECT}))
        self.mqttClient.publish(TOPIC_AK, json.dumps({"clientId" : self.id,"purpose": START_CONNECT}))
        t = threading.Thread(target= self.mainLoop)
        t.start()

    def on_disconnect(self, client, userdata, rc):
        # client.publish(TOPIC_AK, json.dumps({"clientId" : 0,"purpose": END_CONNECT}))
        pass

    def on_message(self, client, userdata, msg):
        print("message -", msg.payload.decode("utf-8"))
        # message = json.loads(msg.payload.decode("utf-8"))


if __name__ == "__main__":
    if DEBUG == True:
        time.sleep(3)
        TestCase().testCase1()