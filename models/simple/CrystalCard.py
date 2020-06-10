import models.simple.Pocket as Pocket
import models.simple.Coin as Coin
import tkinter as tk
class CrystalCard:
    __back=None
    def __init__(self,victoryPoints,coasts,earnings,photo):
        self.__imagePath=photo
        self.__victoryPoints=int(victoryPoints)
        self.__coasts= Pocket.Pocket()
        self.__earnings= Pocket.Pocket()
        self.__image=None
        self.__smalImage=None
        for i in coasts:
            self.__coasts.push(Coin.Coin(i['name'], int(i['count'])))
        for i in earnings:
            self.__earnings.push(Coin.Coin(i['name'], int(i['count'])))
    def __str__(self):
        return f"cardVP: {self.__victoryPoints} Earnings: {self.__earnings.__str__()} Coasts: {self.__coasts.__str__()}"
    def getBack(self):
        if CrystalCard.__back==None:
            CrystalCard.__back=tk.PhotoImage(file="photos\High\cardsBack.png").subsample(2)
        return CrystalCard.__back
    def __getImagePath(self):
        return self.__imagePath
    def getImage(self):
        if self.__image==None:
            self.__image=tk.PhotoImage(file=self.__getImagePath())
        return self.__image
    def getSmallImage(self):
        if self.__smalImage==None:
            self.__smalImage=tk.PhotoImage(file=self.__getImagePath()).subsample(2)
        return self.__smalImage
    def getCoasts(self):
        return self.__coasts
    def getType(self):
        return self.__earnings.getAllCoins()[0].getType()
    def get_victory_points(self):
        return self.__victoryPoints
    def getStatsForConector(self):
        output=[]
        output.append(self.get_victory_points())
        for i in ['ruby','emerald','diamond','onyx','sapphire']:
            output.append(self.__coasts.takeCoinByType(i).getCount())
        for i in ['ruby','emerald','diamond','onyx','sapphire']:
            output.append(self.__earnings.takeCoinByType(i).getCount())
        return output



