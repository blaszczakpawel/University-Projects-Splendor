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
    def take(self,coin):
        if isinstance(coin,C.Coin):
            for i in self.__pocket:
                if i==coin:
                    self.__pocket.remove(i)
                    return i
            else:
                return 0
