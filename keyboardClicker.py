import win32api

from config import VK_CODE, DOWN, UP, BUTTON

tmpKeyP0 = []
tmpKeyP1 = []
tmpKey = [tmpKeyP0, tmpKeyP1]

playerIdList = []
playerDic = {}
playerCursor = 0

class KeyboardClicker:
    def __init__(self):
        pass
    def clickBroker(self, virtualKey, clickType):
        if clickType == DOWN:
            self.keydown(virtualKey)
        elif clickType == UP:
            self.keyup(virtualKey)
        elif clickType == BUTTON:
            self.buttonClick(virtualKey)

    def keydown(self, virtualKey):
        win32api.keybd_event(virtualKey, 0, 0, 0)

    def keyup(self, virtualKey):
        win32api.keybd_event(virtualKey, 0, 2, 0)

    def buttonClick(self, virtualKey):
        win32api.keybd_event(virtualKey, 0, 0, 0)
        win32api.keybd_event(virtualKey, 0, 2, 0)

# def KeyboardClick(playerId, vk):
#     if len(vk) == 2:
#         item1, item2 = vk
#         win32api.keybd_event(item1, 0, 0, 0)
#         win32api.keybd_event(item2, 0, 0, 0)
#
#         if tmpKey[playerId] != vk:
#             for item in tmpKey[playerId]:
#                 win32api.keybd_event(item, 0, 2, 0)
#             tmpKey[playerId] = vk
#     else:
#         item1 = vk[0]
#         win32api.keybd_event(item1, 0, 0, 0)
#
#         if tmpKey[playerId] != vk:
#             for item in tmpKey[playerId]:
#                 win32api.keybd_event(item, 0, 2, 0)
#             tmpKey[playerId] = vk
#
# def KeyUp(playerId, key):
#     if key == "keyup":
#         for item in tmpKey[playerId]:
#                 win32api.keybd_event(item, 0, 2, 0)
#
# def buttonClick(vk):
#     item = vk[0]
#     win32api.keybd_event(item, 0, 0, 0)
#     win32api.keybd_event(item, 0, 2, 0)

# def Delay(sec) :
#     # msec = float(sec) * 1000
#     time.sleep(sec)
#
# def msgToAscii(playerId):
#     if playerId == 1:
#         switcher = {
#             1 : [VK_CODE['w']],
#             2 : [VK_CODE['w'],VK_CODE['d']],
#             3 : [VK_CODE['d']],
#             4 : [VK_CODE['s'],VK_CODE['d']],
#             5 : [VK_CODE['s']],
#             6 : [VK_CODE['s'],VK_CODE['a']],
#             7 : [VK_CODE['a']],
#             8 : [VK_CODE['w'],VK_CODE['a']],
#             9 : [VK_CODE['spacebar']],
#             10 : [VK_CODE['q']],
#             11 : [VK_CODE['e']],
#             12 : "keyup",
#             99 : "onDestroy"
#         }
#         return switcher
#     elif playerId == 0:
#         switcher = {
#             1 : [VK_CODE['up_arrow']],
#             2 : [VK_CODE['up_arrow'],VK_CODE['right_arrow']],
#             3 : [VK_CODE['right_arrow']],
#             4 : [VK_CODE['down_arrow'],VK_CODE['right_arrow']],
#             5 : [VK_CODE['down_arrow']],
#             6 : [VK_CODE['down_arrow'],VK_CODE['left_arrow']],
#             7 : [VK_CODE['left_arrow']],
#             8 : [VK_CODE['up_arrow'],VK_CODE['left_arrow']],
#             9 : [VK_CODE['/']],
#             10 : [VK_CODE[',']],
#             11 : [VK_CODE['.']],
#             12 : "keyup",
#             99 : "onDestroy"
#         }
#         return switcher