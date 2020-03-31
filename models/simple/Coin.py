class Coin:
    def __init__(self, type,count):
        self.__type=type
        self.__count=int(count)
    def __str__(self):
        return f'{self.__count} of {self.__type}'
    def getType(self):
        return self.__type
