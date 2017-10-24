class ClientManager:
    def __init__(self):
        self.clientList = []
        self.clientNum = 0

    def appendNewClient(self, clientId):
        self.clientList.append(clientId)
        self.clientNum += 1

    def removeClient(self, clientId):
        self.clientList.remove(clientId)
        self.clientNum -= 1

    def isNewClient(self, clientId):
        if clientId in self.clientList:
            return True
        else:
            return False