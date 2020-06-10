import xml.etree.ElementTree as xml
import models.simple.crystalcard as CC
import random as ran

class CrystalCardDeck:
    def __init__(self, path):
        self.__cards=[]

        tree = xml.parse(path)
        root = tree.getroot()

        for card in root:
            self.__cards.append(CC.CrystalCard(card))
    def getRandomCard(self):
        rand=int(ran.random()*len(self.__cards))
        data = self.__cards[rand]
        del self.__cards[rand]
        return data

