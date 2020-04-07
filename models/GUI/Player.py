import tkinter as tk
import models.game.Player as P
import models.GUI.Frame as F
class Player:
    def __init__(self,root,player):
        self.__player=player
        self.__crystals={}
        self.__frame=F.Frame(root)
        for i in [['diamond',1,1],['emerald',1,2],['sapphire',1,3],['ruby',1,4],['onyx',1,5],['gold',1,6]]:
            self.__crystals[i[0]]={}
            coin=self.__player.getPocket().takeCoinByType(i[0])
            self.__crystals[i[0]]['frame']=F.Frame(self.__frame.getFrame())
            self.__crystals[i[0]]['frame'].getFrame().grid(row=1,column=i[2])
            self.__crystals[i[0]]['coinCountLabel']=tk.Label(self.__crystals[i[0]]['frame'].getFrame(),text=coin.getCount())
            self.__crystals[i[0]]['coinCountLabel'].grid(column=0,row=i[1]+0)
            self.__crystals[i[0]]['coinPhotoLabel']=tk.Label(self.__crystals[i[0]]['frame'].getFrame(),image=coin.getImage())
            self.__crystals[i[0]]['coinPhotoLabel'].grid(column=0,row=i[1]+1)
    def getFrame(self):
        return self.__frame.getFrame()
    def refresh(self):
        print(f"odświerzam gracza {self.__player.getName()}")
        for i in ['diamond','emerald','sapphire','ruby','onyx','gold']:
            self.__crystals[i]['coinCountLabel'].configure(text=self.__player.getPocket().takeCoinByType(i).getCount())
