import time
import paho.mqtt.client as mqtt
import win32con
import win32api

from config import TOPIC_AP, IP, VK_CODE

tmpKeyP0 = []
tmpKeyP1 = []
tmpKey = [tmpKeyP0, tmpKeyP1]

playerIdList = []
playerDic = {}
playerCursor = 0

def KeyboardClick(playerId, vk) :
    if len(vk) == 2:
        item1, item2 = vk
        win32api.keybd_event(item1, 0, 0, 0)
        win32api.keybd_event(item2, 0, 0, 0)

        if tmpKey[playerId] != vk:
            for item in tmpKey[playerId]:
                win32api.keybd_event(item, 0, 2, 0)
            tmpKey[playerId] = vk
    else:
        item1 = vk[0]
        win32api.keybd_event(item1, 0, 0, 0)

        if tmpKey[playerId] != vk:
            for item in tmpKey[playerId]:
                win32api.keybd_event(item, 0, 2, 0)
            tmpKey[playerId] = vk

def KeyUp(playerId, key):
    if key == "keyup":
        for item in tmpKey[playerId]:
                win32api.keybd_event(item, 0, 2, 0)

def buttonClick(vk):
    item = vk[0]
    win32api.keybd_event(item, 0, 0, 0)
    win32api.keybd_event(item, 0, 2, 0)

def Delay(sec) :
    # msec = float(sec) * 1000
    time.sleep(sec)

def msgToAscii(playerId):
    if playerId == 1:
        switcher = {
            1 : [VK_CODE['w']],
            2 : [VK_CODE['w'],VK_CODE['d']],
            3 : [VK_CODE['d']],
            4 : [VK_CODE['s'],VK_CODE['d']],
            5 : [VK_CODE['s']],
            6 : [VK_CODE['s'],VK_CODE['a']],
            7 : [VK_CODE['a']],
            8 : [VK_CODE['w'],VK_CODE['a']],
            9 : [VK_CODE['spacebar']],
            10 : [VK_CODE['q']],
            11 : [VK_CODE['e']],
            12 : "keyup",
            99 : "onDestroy"
        }
        return switcher
    elif playerId == 0:
        switcher = {
            1 : [VK_CODE['up_arrow']],
            2 : [VK_CODE['up_arrow'],VK_CODE['right_arrow']],
            3 : [VK_CODE['right_arrow']],
            4 : [VK_CODE['down_arrow'],VK_CODE['right_arrow']],
            5 : [VK_CODE['down_arrow']],
            6 : [VK_CODE['down_arrow'],VK_CODE['left_arrow']],
            7 : [VK_CODE['left_arrow']],
            8 : [VK_CODE['up_arrow'],VK_CODE['left_arrow']],
            9 : [VK_CODE['/']],
            10 : [VK_CODE[',']],
            11 : [VK_CODE['.']],
            12 : "keyup",
            99 : "onDestroy"
        }
        return switcher

def getPlayerId(clientId):
    global playerCursor
    if clientId not in playerIdList:
        playerIdList.append(clientId)
        playerDic[clientId] = playerCursor
        playerCursor += 1
        id = playerDic[clientId]
        print(playerDic)
    elif playerDic[clientId] != None:
        id = playerDic[clientId]
    else:
        tmpV = False
        tmpV2 = -1
        for key, value in playerDic.item():
            if value in [0,1]:
                tmpV = True
                tmpV2 = value
        if tmpV == False:
            playerDic[clientId] = tmpV2
        else:
            playerDic[clientId] = playerCursor
            playerCursor += 1
        id = playerDic[clientId]
    return id

def playerManager(playerId, clientId, onState):
    playerIdList.remove(playerId)
    playerDic = {key: value for key, value in playerDic.items() if value is not playerId}
    print (playerDic)
    if onState == "onDestroy":
        if playerId in [0,1]:
            a = 100
            tmpDicKey = None
            for key, value in playerDic.item():
                if value <= a and value not in [0,1]:
                    a = value
                    tmpDicKey = key
            if tmpDicKey != None:
                playerDic[tmpDicKey] = a



def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    message = str(msg.payload)[2:-1]
    mlist = []
    mlist = message.split('+')

    clientId = mlist[0]

    print (clientId + " - " + message)

    # if mlist[0]== '12':
    # 	pSwitcher = "keyup"
    # else:
    playerId = getPlayerId(mlist[0])
    pSwitcher = msgToAscii(playerId)

    actionInt = int(mlist[1])
    if actionInt in [9,10,11]:
        buttonClick(pSwitcher[actionInt])
    elif actionInt in [1,2,3,4,5,6,7,8]:
        KeyboardClick(playerId, pSwitcher[actionInt])
    elif actionInt in [12]:
        KeyUp(playerId, pSwitcher[actionInt])
    elif actionInt in [99]:
        playerManager(playerId, clientId, pSwitcher[actionInt])
    # KeyboardClick([0x0002])
    # Delay(0.05)
    # client.publish(topicAp, None,0,True)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to -", TOPIC_AP)

def connect2mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message #callback
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    try:
        client.connect(IP, 1883, 30)
        # client.connect("117.16.136.159", 1883, 30)

        client.subscribe(TOPIC_AP)
        print("Subscribed to -", TOPIC_AP)

        # mqttc.publish(“hello/world”, “Hello, World!”)

        client.loop_forever()

    except Exception as e:
        print(e)
        print("Connection on Failure")
        main()

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("192.168.123.100", 1883, 30)
        # client.connect("117.16.136.159", 1883, 30)
        print("Connection on Success")

        client.subscribe(TOPIC_AP)
        print("Subscribed to - " + TOPIC_AP)

        # mqttc.publish(“hello/world”, “Hello, World!”)

        client.loop_forever()

    except Exception as e:
        print(e)
        print("Connection on Failure")
        main()

if __name__ == '__main__':
    main()
