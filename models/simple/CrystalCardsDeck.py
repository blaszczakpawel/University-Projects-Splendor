import json
import models.simple.CrystalCard as CC
class CrystalCardDeck:
    def __init__(self,path):
        self.__deck=[]
        with open(path, 'r') as f:
            distros_dict = json.load(f)
        for i in distros_dict:
            self.__deck.append(CC.CrystalCard(i['victoryPoints'],i['coasts'],i['earnings'],i['photo']))
    def getNext(self):
        if len(self.__deck)!=0:
            pom=self.__deck[0]
            self.__deck.remove(pom)
            return pom
