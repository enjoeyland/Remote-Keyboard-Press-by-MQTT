from config import MAXIMUM_PLAYER_NUM, MINIMUM_PLAYER_NUM


class PlayerManager:
    def __init__(self, ClientManager):
        self.mClientManager = ClientManager
    def isPlayer(self, clientId):
        if clientId in self.mClientManager.clientList[:MAXIMUM_PLAYER_NUM]:
            return True
        else:
            return False
    def isPlayerIsEnough(self):
        if self.mClientManager.clientNum >= MINIMUM_PLAYER_NUM:
            return True
        else:
            return False


# def getPlayerId(clientId):
#     global playerCursor
#     if clientId not in playerIdList:
#         playerIdList.append(clientId)
#         playerDic[clientId] = playerCursor
#         playerCursor += 1
#         id = playerDic[clientId]
#         print(playerDic)
#     elif playerDic[clientId] != None:
#         id = playerDic[clientId]
#     else:
#         tmpV = False
#         tmpV2 = -1
#         for key, value in playerDic.item():
#             if value in [0,1]:
#                 tmpV = True
#                 tmpV2 = value
#         if tmpV == False:
#             playerDic[clientId] = tmpV2
#         else:
#             playerDic[clientId] = playerCursor
#             playerCursor += 1
#         id = playerDic[clientId]
#     return id
#
# def playerManager(playerDic, playerId, clientId, onState):
#     playerIdList.remove(playerId)
#     playerDic = { key: value for key, value in playerDic.items() if value is not playerId }
#     # print (playerDic)
#     if onState == "onDestroy":
#         if playerId in [0,1]:
#             a = 100
#             tmpDicKey = None
#             for key, value in playerDic.item():
#                 if value <= a and value not in [0,1]:
#                     a = value
#                     tmpDicKey = key
#             if tmpDicKey != None:
#                 playerDic[tmpDicKey] = a

