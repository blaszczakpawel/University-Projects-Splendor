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
<<<<<<< Updated upstream
    def getCrystalCard(self,x,y):
        return self.__cards[x][y]
=======
    def getCard(self,x,y):
        return self.__cards[x][y]
    def getCoinByType(self,type):
        return self.__coins.takeCoinByType(type)
    def getCoins(self):
        return self.__coins
    def removeCard(self,card):
        for i in [['high',1],['medium',2],['low',3]]:
            if card in self.__cards[i[1]]:
                self.__cards[i[1]].remove(card)
    def updateCardsAndLords(self):
        if len(self.__cards[0])<4:
            self.__cards[0].append(self.__decks['lords'].getNext())
        for i in [['high',1],['medium',2],['low',3]]:
            if len(self.__cards[i[1]])!=4:
                self.__cards[i[1]].append(self.__decks[i[0]].getNext())
    def getLordById(self,number):
        return self.__cards[0][number]
    def removeLord(self,lord):
        self.__cards[0].remove(lord)
>>>>>>> Stashed changes
