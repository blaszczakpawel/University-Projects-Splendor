import models.simple.Pocket as Pocket
import models.simple.Coin as Coin
import tkinter as tk
class CrystalCard:
    def __init__(self,victoryPoints,coasts,earnings,photo):
        self.__imagePath=photo
        self.__victoryPoints=victoryPoints
        self.__coasts= Pocket.Pocket()
        self.__earnings= Pocket.Pocket()
        self.__image=None
        for i in coasts:
            self.__coasts.push(Coin.Coin(i['name'], i['count']))
        for i in earnings:
            self.__earnings.push(Coin.Coin(i['name'], i['count']))
    def __getImagePath(self):
        return self.__imagePath
    def getImage(self):
        if self.__image==None:
            self.__image=tk.PhotoImage(file=self.__getImagePath())
        return self.__image



