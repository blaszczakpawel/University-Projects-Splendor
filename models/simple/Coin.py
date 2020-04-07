import tkinter as tk
class Coin:
    __images={}
    def __init__(self, type,count):
        self.__type=type
        self.__count=int(count)
    def __str__(self):
        return f'{self.__count} of {self.__type}'
    def getType(self):
        return self.__type
    def getCount(self):
        return self.__count
    def getCoin(self,count):
        if self.__count-count>=0:
            return count
        return 0
    def changeCount(self,count):
        self.__count+=count
    def getImage(self):
        if self.getType() not in Coin.__images.keys():
            Coin.__images[self.getType()]=tk.PhotoImage(file=f"photos/Coins/{self.getType()}.png").subsample(2)
        return Coin.__images[self.getType()]

