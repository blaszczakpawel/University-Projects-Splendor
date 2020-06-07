import tkinter as tk
import models.game.Player as P
import models.GUI.Frame as F
class Player:
    def __init__(self,root,player,board):
        self.__player=player
        self.__crystals={}
        self.__frame=F.Frame(root)
        self.__board=board

        self.__crystals['main']={}
        self.__crystals['main']['frame']=F.Frame(self.__frame.getFrame())
        self.__crystals['main']['frame'].getFrame().grid(column=0,row=0)
        self.__crystals['main']['vp']=tk.Label(  self.__crystals['main']['frame'].getFrame(),text="VP: 0")
        self.__crystals['main']['vp'].grid(column=0,row=0)
        for i in [['diamond',1,5],['emerald',1,4],['sapphire',1,3],['ruby',1,2],['onyx',1,1],['gold',1,6]]:
            self.__crystals[i[0]]={}
            self.__crystals[i[0]]['frame']=F.Frame(self.__frame.getFrame())
            self.__crystals[i[0]]['frame'].getFrame().grid(row=1,column=i[2])
            #lordowie
            self.__crystals[i[0]]['lord']=tk.Label(self.__crystals[i[0]]['frame'].getFrame())
            self.__crystals[i[0]]['lord'].grid(column=0,row=i[1])
            #coinsy
            coin=self.__player.getPocket().takeCoinByType(i[0])
            self.__crystals[i[0]]['coinCountLabel']=tk.Label(self.__crystals[i[0]]['frame'].getFrame(),text=coin.getCount())
            self.__crystals[i[0]]['coinCountLabel'].grid(column=0,row=i[1]+1)
            self.__crystals[i[0]]['coinPhotoLabel']=tk.Label(self.__crystals[i[0]]['frame'].getFrame(),image=coin.getImage())
            self.__crystals[i[0]]['coinPhotoLabel'].grid(column=0,row=i[1]+2)
            #cards
            cards=self.__player.getCardsByType(i[0])
            self.__crystals[i[0]]['cardsCountLabel']=tk.Label(self.__crystals[i[0]]['frame'].getFrame(),text=len(cards))
            self.__crystals[i[0]]['cardsCountLabel'].grid(column=0,row=i[1]+3)

            self.__crystals[i[0]]['cardsPhotoLabel']=tk.Label(self.__crystals[i[0]]['frame'].getFrame(),image=self.__board.getCard(1,1).getBack())
            self.__crystals[i[0]]['cardsPhotoLabel'].grid(column=0,row=i[1]+4)

    def getFrame(self):
        return self.__frame.getFrame()
    def refresh(self):
        #print(f"odświerzam gracza {self.__player.getName()}")
        self.__crystals['main']['vp'].configure(text=f"VP: {self.__player.getVictoryPoints()}")
        lords = self.__player.getLords()
        counter=0
        for i in ['diamond','emerald','sapphire','ruby','onyx','gold']:
            self.__crystals[i]['coinCountLabel'].configure(text=self.__player.getPocket().takeCoinByType(i).getCount())
            if len(self.__player.getCardsByType(i))>0:
                self.__crystals[i]['cardsCountLabel'].configure(text=len(self.__player.getCardsByType(i)))
                self.__crystals[i]['cardsPhotoLabel'].configure(image=self.__player.getCardsByType(i)[len(self.__player.getCardsByType(i)) - 1].getSmallImage())
            else:
                self.__crystals[i]['cardsPhotoLabel'].configure(image=self.__board.getCard(1,1).getBack())
            if counter<len(lords):
                self.__crystals[i]['lord'].configure(image=lords[counter].getSmallImage())
                counter+=1


