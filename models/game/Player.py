import models.simple.Pocket as P
import models.simple.Coin as C
class Player:
    def __init__(self,name):
        self.__name=name
        self.__victoryPoints=0
        self.__lords=[]
        self.__pocet=P.Pocket()
        self.__cards={}
        for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby','gold']:
            self.__pocet.push(C.Coin(i, 0))
            self.__cards[i]=[]
    def getPocket(self):
        return self.__pocet
    def getName(self):
        return self.__name
    def getCardsCounts(self):
        count=0
        for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby', 'gold']:
            count+=len(self.__cards[i])
        return count
    def getCardsCountByType(self,type):
        return len(self.__cards[type])
    def getLastCardByType(self,type):
        return self.__cards[type][len(self.__cards[type])]
    def getCards(self):
        return self.__cards
    def getLords(self):
        return self.__lords
    def getCardsByType(self,type):
        return self.__cards[type]
    def addCard(self,card):
        self.__cards[card.getType()].append(card)
    def addCardToReservation(self,card):
        self.__cards['gold'].append(card)
    def addLord(self,lord):
        self.__lords.append(lord)
    def addVicotorypoints(self,points):
        self.__victoryPoints+=points
    def getVictoryPoints(self):
        return self.__victoryPoints