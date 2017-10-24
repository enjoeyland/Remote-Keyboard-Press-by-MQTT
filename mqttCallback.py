import time
import win32con
import win32api
import json
import logging

from clientManager import ClientManager
from config import TOPIC_AP, VK_CODE, MAXIMUM_PLAYER_NUM, END_CONNECT, ACTION
from keyboardClicker import KeyboardClicker
from notifyToClient import NotifyToClient
from playerManager import PlayerManager



class MqttCallback:
    def __init__(self):
        self.mClientManager = ClientManager()
        self.mPlayerManager = PlayerManager(self.mClientManager)
        self.mNotifyToClient = NotifyToClient()
        self.mKeyboardClicker = KeyboardClicker()

    def on_connect(self, client, userdata, flags, rc):
        print("on_connect", client, userdata, flags, rc)
        print("Connection on Success")
        print("my client id -", client)

    def on_message(self, client, userdata, msg):
        # print("on_message",client, userdata, msg)
        print(msg.payload.decode("utf-8"), "-", client)

        # message = msg.payload.decode('utf-8')
        message = json.loads(msg.payload.decode("utf-8"))
        # mlist = []
        # mlist = message.split()

        clientId = message["clientId"]

        # if mlist[0]== '12':
        # 	pSwitcher = "keyup"
        # else:

        # String uniqueID = UUID.randomUUID().toString(); #java android unique Id

        if self.mClientManager.isNewClient(clientId):
            print("new client connected" + clientId)
            self.mClientManager.appendNewClient(clientId)
            self.mNotifyToClient.updateClientNum()

        if self.mPlayerManager.isPlayer(clientId) == True:
            if message["state"] == END_CONNECT:
                self.mClientManager.removeClient(clientId)
                self.mNotifyToClient.notifyOppositePlayerDisconnect()
                self.mNotifyToClient.updateClientNum()

                if self.mPlayerManager.isPlayerIsEnough():
                    self.mNotifyToClient.notifyYourPlayer(self.mClientManager.clientList[MAXIMUM_PLAYER_NUM])
                else:
                    self.mNotifyToClient.notifyPlayerIsNotEnough()

            elif message["state"] == ACTION:
                self.mKeyboardClicker.clickBroker(message["virtualKey"], message["clickType"])

        else:
            if message["state"] == END_CONNECT:
                self.mClientManager.removeClient(clientId)


        #####################################
        # playerId = getPlayerId(clientId)
        # pSwitcher = msgToAscii(playerId)
        #
        # actionInt = message["actionInt"]
        # if actionInt in [9,10,11]:
        #     buttonClick(pSwitcher[actionInt])
        # elif actionInt in [1,2,3,4,5,6,7,8]:
        #     KeyboardClick(playerId, pSwitcher[actionInt])
        # elif actionInt in [12]:
        #     KeyUp(playerId, pSwitcher[actionInt])
        # elif actionInt in [99]:
        #     playerManager(playerId, clientId, pSwitcher[actionInt])


        # KeyboardClick([0x0002])
        # Delay(0.05)
        # client.publish(topicAp, None,0,True)


    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")

    def on_subscribe(self, client, userdata, mid, granted_qos):
        # print("on_subscribe",client, userdata, mid, granted_qos)
        print("Subscribed to",TOPIC_AP)

    def on_unsubscribe(self, client, userdata, mid):
        # if self.mPlayerManager.isPlayer(client) == True:
        #     self.mClientManager.removeClient(client)
        #     self.mNotifyToClient.notifyOppositePlayerDisconnect()
        #     self.mNotifyToClient.updateClientNum()
        #
        #     if self.mPlayerManager.isPlayerIsEnough():
        #         self.mNotifyToClient.notifyYourPlayer(self.mClientManager.clientList[MAXIMUM_PLAYER_NUM])
        #     else:
        #         self.mNotifyToClient.notifyPlayerIsNotEnough()
        #
        # else:
        #     self.mClientManager.removeClient(client)
        pass

    def on_publish(self, client, userdata, mid):
        # print("on_publish",client, userdata, mid)
        print("published")


# def removeByteFromMessage(message):
#     return str(message)[2:-1]
#
# def connect2mqtt():
#     client = mqtt.Client()
#     client.on_connect = on_connect
#     client.on_message = on_message #callback
#     client.on_disconnect = on_disconnect
#     client.on_subscribe = on_subscribe
#
#     try:
#         client.connect(IP, port = PORT, keepalive = 30)
#         # client.connect("117.16.136.159", 1883, 30)
#
#         client.subscribe(TOPIC_AP)
#         print("Subscribed to -", TOPIC_AP)
#
#         # mqttc.publish(“hello/world”, “Hello, World!”)
#
#         client.loop_forever()
#
#     except Exception as e:
#         print(e)
#         print("Connection on Failure")
#         main()
