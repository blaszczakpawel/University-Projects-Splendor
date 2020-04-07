import models.simple.CrystalCardsDeck as CCD
import models.simple.LordsDeck as LD
import tkinter as tk
import models.simple.Pocket as P
import models.simple.Coin as C

import os
class Board:
    def __init__(self):
        self.__decks={}
        self.__cards = [[]]
        self.__coins=P.Pocket()
        self.__coins.push(C.Coin('gold', 5))
        for i in ['diamond','emerald','sapphire','onyx','ruby']:
            self.__coins.push(C.Coin(i,7))
        self.__lords=LD.LordsDeck("cards\LordsList.json")
        for i in [['low','cards\LowCrystalList.json'],['medium','cards\MediumCrystalList.json'],['high','cards\HighCrystalList.json']]:
            self.__decks[i[0]]=CCD.CrystalCardDeck(i[1])
        self.__decks['lords']=LD.LordsDeck('cards\LordsList.json')
        for i in range(4):
            self.__cards[0].append(self.__lords.getNext())
        for i in [['high',1],['medium',2],['low',3]]:
            self.__cards.append([])
            for j in range(4):
                self.__cards[i[1]].append(self.__decks[i[0]].getNext())
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
