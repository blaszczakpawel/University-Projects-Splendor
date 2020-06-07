import tkinter as tk
class Lord:
    def __init__(self,victoryPoints,photo,coasts):
        self.__vicotryPoints=victoryPoints
        self.__photo=photo
        self.__coasts=coasts
        self.__image=None
        self.__smallImage=None
    def __getImagePath(self):
        return self.__photo
    def getImage(self):
        if self.__image==None:
            self.__image=tk.PhotoImage(file=self.__getImagePath())
        return self.__image
    def getSmallImage(self):
        if self.__smallImage==None:
            self.__smallImage=tk.PhotoImage(file=self.__getImagePath()).subsample(2)
        return self.__smallImage
    def getCoasts(self):
        return self.__coasts
    def getvictoryPoints(self):
        return self.__vicotryPoints
    def getLordStatsForConector(self):
        output=[]
        output.append(self.getvictoryPoints())
        for i in ['ruby','emerald','diamond','onyx','sapphire']:
            if i in self.__coasts:
                output.append(self.__coasts[i])
            else:
                output.append(0)
        return output
