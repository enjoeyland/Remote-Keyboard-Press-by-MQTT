import json
import paho.mqtt.client as mqtt

from config import IP, PORT, TOPIC_AP
from mqttCallback import MqttCallback


def main():
    mqttClient = mqtt.Client()
    mMqttCallback = MqttCallback()

    mqttClient.on_connect = mMqttCallback.on_connect
    mqttClient.on_message = mMqttCallback.on_message
    mqttClient.on_subscribe = mMqttCallback.on_subscribe
    mqttClient.on_publish = mMqttCallback.on_publish

    # try:
    mqttClient.connect(IP, port = PORT, keepalive = 30)
    # client.connect("117.16.136.159", 1883, 30)

    mqttClient.subscribe(TOPIC_AP)

    mqttClient.publish(TOPIC_AP, json.dumps({"clientId" : 0,"state":0}))

    mqttClient.loop_forever()

    # except Exception as e:
    #     print(e)
    #     print("Connection on Failure")
        # main()


if __name__ == '__main__':
    main()