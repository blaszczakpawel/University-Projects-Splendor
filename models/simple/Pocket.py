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
<<<<<<< Updated upstream
    def take(self,coin):
        if isinstance(coin,C.Coin):
            for i in self.__pocket:
                if i==coin:
                    self.__pocket.remove(i)
                    return i
            else:
                return 0
=======
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
            return C.Coin(typeVariable,0)
    def getAllCoins(self):
        return self.__pocket


>>>>>>> Stashed changes
