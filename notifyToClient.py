import json

from config import TOPIC_KA, OPPOSITE_PLAYER_DISCONNECT_MSG, PLAYER_IS_NOT_ENOUGH_MSG, CLIENT_NUM_UPDATED_MSG, \
    YOUR_NOW_PLAYER_MSG


class NotifyToClient:
    def __init__(self, mqttClient):
        self.mqttClient = mqttClient

    def notifyOppositePlayerDisconnect(self):
        self.mqttClient.publish(TOPIC_KA, self._msgJsonDump(OPPOSITE_PLAYER_DISCONNECT_MSG))

    def notifyPlayerIsNotEnough(self):
        self.mqttClient.publish(TOPIC_KA, self._msgJsonDump(PLAYER_IS_NOT_ENOUGH_MSG))

    def updateClientNum(self):
        self.mqttClient.publish(TOPIC_KA, self._msgJsonDump(CLIENT_NUM_UPDATED_MSG))

    def notifyYourPlayer(self, clientId):
        self.mqttClient.publish(TOPIC_KA, self._msgJsonDump(YOUR_NOW_PLAYER_MSG, clientId = clientId))

    def _msgJsonDump(self, msg, **kwargs):
        msgDic = {**{"notify" : msg}, **kwargs}
        return json.dumps(msgDic)