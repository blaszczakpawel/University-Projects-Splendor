import models.simple.Pocket as Pocket
import models.simple.Coin as Coin
class CrystalCard:
    def __init__(self,victoryPoints,coasts,earnings,photo):
        self.__photo=photo
        self.__victoryPoints=victoryPoints
        self.__coasts= Pocket.Pocket()
        self.__earnings= Pocket.Pocket()
        for i in coasts:
            self.__coasts.push(Coin.Coin(i['name'], i['count']))
        for i in earnings:
            self.__earnings.push(Coin.Coin(i['name'], i['count']))
    def getImagePath(self):
        return self.__photo

