import models.simple.CrystalCardsDeck as CCD
import models.simple.LordsDeck as LD
import tkinter as tk

import os
class Board:
    def __init__(self):
        self.__decks={}
        for i in [['low','cards\LowCrystalList.json'],['medium','cards\MediumCrystalList.json'],['high','cards\HighCrystalList.json']]:
            self.__decks[i[0]]=CCD.CrystalCardDeck(i[1])
        self.__decks['lords']=LD.LordsDeck('cards\LordsList.json')
        self.__cards=[]
        for i in [['low',0]]:
            self.__cards.append([])
            for j in range(4):
                self.__cards[i[1]].append(self.__decks[i[0]].getNext())
    def getCrystalCard(self,x,y):
        return self.__cards[x][y]