import models.simple.coin as coin

class Pocket:
    def __init__(self):
        self.__pocket = []
    def push(self, coin_to_push):
        if isinstance(coin_to_push, coin.Coin):
            self.__pocket.append(coin_to_push)
    def coins_count(self):
        return sum(x.get_count() for x in self.__pocket)
    def take_coin_by_type(self, type_variable):
        for i in range(len(self.__pocket)):
            if str(type_variable) == str(self.__pocket[i].get_type()):
                return self.__pocket[i]
        else:
            return coin.Coin(type_variable, 0)
    def get_all_coins(self):
        return self.__pocket


