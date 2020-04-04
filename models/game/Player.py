import models.simple.Pocket as P
import models.simple.Coin as C
class Player:
    def __init__(self,name):
        self.__name=name
        self.__pocet=P.Pocket()
        for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby','gold']:
            self.__pocet.push(C.Coin(i, 0))
    def getPocket(self):
        return self.__pocet
    def getName(self):
        return self.__name