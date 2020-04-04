import models.simple.Coin as C
class Pocket:
    def __init__(self):
        self.__pocket=[]
    def __str__(self):
        output=''
        for i in self.__pocket:
            output+=i.__str__()+'\n'
        return output
    def push(self,coin):
        if isinstance(coin,C.Coin):
            self.__pocket.append(coin)
    def coinsCount(self):
        counter=0
        for i in self.__pocket:
            counter+=i.getCount()
        return counter
    def takeCoinByType(self,typeVariable):
        for i in range(len(self.__pocket)):
            if str(typeVariable)==str(self.__pocket[i].getType()):
                return self.__pocket[i]
        else:
            print(self)
            raise Exception(f"{typeVariable} {type(typeVariable)} no niema ziom")
    def getAllCoins(self):
        return self.__pocket


