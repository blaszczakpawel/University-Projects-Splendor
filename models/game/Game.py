import models.game.Board as B
import models.game.Player as P
import models.simple.Pocket as PC
import models.simple.Coin as C
import models.GUI.GUI as G
import tkinter as tk
import models.conector.mainConecotr as c
import json
import models.neuralNetwork.NeuralNetwork as Network
class Game:
    __instance=None
    class __Game:
        def __init__(self):
            self.__players={}
            self.__actualPlayer = "one"
            self.__board = B.Board()
            self.__round=0
            self.__isGui=True
            self.__AI=c.mainConecotr(0,'AI/Brutus')
            self.__AI.loadObject()
            for i in ['one','two']:
                self.__players[i]=P.Player(i)
        def __loadAi(self):
            with open("AI/Brutus_0.json", 'r') as json_file:
                data = json.load(json_file)
                pom=Network.NeuralNetwork()
                pom.transformFromObject(data['neuralNetwork'])
                self.__AI=c.mainConecotr(8,'AI/Brutus',Obj=pom)
                json_file.close()
        def printStats(self):
            linia=f"\t\t{self.__round} "
            for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby','gold']:
                linia+=f" {self.__board.getCoinByType(i).getCount()}"
            print(linia)

            for i in ['one','two']:
                print(f"\t\t{i}: {self.__players[i].getVictoryPoints()} {len(self.__players[i].getLords())}")
                linia='\t\t'
                for j in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby','gold']:
                    linia+=f"{self.__players[i].getCoinCountByType(j)} "
                print(linia)
                linia = '\t\t'
                for j in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby', 'gold']:
                    linia += f"{self.__players[i].getCardsCountByType(j)} "
                print(f"{linia}")
            print("\n")


        def runBetweenIA(self, first, second, generation):
            #print(f"\tStart walki {first.getNumber()} vs {second.getNumber()}")
            self.__isGui=False
            vicotry=0
            counterOfPasses=0
            counterOfPassesOne=0
            counterOfPassesTwo=0
            while 5>1:
                #self.printStats()
                #print(f"\t\trunda {self.__round} wynik {self.__players['one'].getVictoryPoints()} do {self.__players['two'].getVictoryPoints()}")
                if self.__round>400:
                    #print(f"\tKoniec walki za dużo rund")
                    return [0,0,0]
                if counterOfPasses==5:
                    #print(f"\tKoniec walki za dużo passes")
                    return [-1, -1, 0]
                if counterOfPassesOne==10:
                    return [-1,0,0]
                if counterOfPassesTwo==10:
                    return [0,-1,0]
                pom=first.run(self,'one',generation)
                self.move(pom)
                #print("\t\t\tOne wykonal ruch")
                pom2=second.run(self,'two',generation)
                self.move(pom2)
                if pom2==[{"type":"pass"}] and pom==[{"type":"pass"}]:
                    counterOfPasses+=1
                else:
                    counterOfPasses=0
                if pom==[{"type":"pass"}]:
                    counterOfPassesOne+=1
                else:
                    counterOfPassesOne=0
                if pom2==[{"type":"pass"}]:
                    counterOfPassesTwo+=1
                else:
                    counterOfPassesTwo=0
                #print("\t\t\tTwo wykonal ruch")
                if self.__players['one'].getVictoryPoints() >= 15 or self.__players['two'].getVictoryPoints() >= 15:
                    if self.__players['one'].getVictoryPoints() > self.__players['two'].getVictoryPoints():
                        #print(f"\tKoniec walki {self.__round} {self.__players['one'].getVictoryPoints()} do {self.__players['two'].getVictoryPoints()}")
                        return [self.__players['one'].getVictoryPoints(), self.__players['two'].getVictoryPoints(),self.__round]
                    if self.__players['one'].getVictoryPoints() < self.__players['two'].getVictoryPoints():
                        #print(f"\tKoniec walki {self.__round} {self.__players['one'].getVictoryPoints()} do {self.__players['two'].getVictoryPoints()}")
                        return [self.__players['one'].getVictoryPoints(),self.__players['two'].getVictoryPoints(),self.__round]
        def getPlayer(self,str):
            if str=='actual':
                return self.__players[self.__actualPlayer]
            return self.__players[str]
        def getActualPlayer(self):
            return self.__actualPlayer
        def getOponent(self):
            if self.__actualPlayer=='one':
                return 'two'
            return 'one'
        def getBoard(self):
            return self.__board
        def setup(self):
            self.__gui = G.GUI(self)
            tk.mainloop()
        def move(self,str):
            self.__move(str)
            if self.__actualPlayer=='two':
                self.__move(self.__AI.run(self,'two',0))
        def __move(self,str):
            output=0
            if len(str)==1:
                if str[0]['type']=='lord':
                    output=moveTakeLord(self.__board,self.__players[self.__actualPlayer],str)
                elif str[0]['type']=='card':
                    output=moveTakeCard(self.__board,self.__players[self.__actualPlayer],str)
                elif str[0]['type']=="pass":
                    output=1
                elif str[0]['type']=='byGoldenCard':
                    output=moveByGoldenCard(self.__board,self.__players[self.__actualPlayer],str)
                else:
                    output=-1
            elif len(str)==2:
                if str[0]['type']=='coin' and str[1]['type']=='coin' and str[0]['name']==str[1]['name'] and str[0]['name']!='gold':
                    output=moveTakeTwoCoins(self.__board.getCoins(),self.__players[self.__actualPlayer].getPocket(),str)
                elif str[0]['type']=='coin' and str[0]['name']=='gold' and str[1]['type']=='card':
                    output=moveReservationCard(self.__board,self.__players[self.__actualPlayer],str)
                else:
                    output=-1
            elif len(str)==3:
                if str[0]['type']=='coin' and str[1]['type']=='coin' and str[2]['type']=='coin' and str[0]['name']!=str[1]['name'] and str[0]['name']!=str[2]['name'] and str[2]['name']!=str[1]['name']and str[0]['name']!='gold'and str[1]['name']!='gold'and str[2]['name']!='gold':
                    output=moveTakeCoin(self.__board.getCoins(),self.__players[self.__actualPlayer].getPocket(),str)
            else:
                raise Exception("Zła ilość poleceń")
            #zamieniam graczy
            if output==1:
                if self.__actualPlayer=="one":
                    self.__actualPlayer="two"
                else:
                    self.__actualPlayer="one"
                    self.__round+=1
                    if self.__players['one'].getVictoryPoints()>=2 or self.__players['two'].getVictoryPoints()>=2:
                        if self.__players['one'].getVictoryPoints()>self.__players['two'].getVictoryPoints():
                            self.__gui.win('one')
                        if self.__players['one'].getVictoryPoints()<self.__players['two'].getVictoryPoints():
                            self.__gui.win('two')
            elif self.__isGui==False:
                raise Exception("NO TE SZTUCZNE TO POJEBALO JE COS")
            if self.__isGui==True:
                self.__gui.refresh()



        def moveCheck(self,str,player):
            playerToCheck=self.__actualPlayer
            if player !=None:
                playerToCheck=player
            output=0
            if len(str)==1:
                if str[0]['type']=='lord':
                    output=moveTakeLordCheck(self.__board,self.__players[playerToCheck],str)
                elif str[0]['type']=='card':
                    output=moveTakeCardCheck(self.__board,self.__players[playerToCheck],str)
                elif str[0]['type']=="pass":
                    output=1
                elif str[0]['type']=='byGoldenCard':
                    output=moveByGoldenCardCheck(self.__board,self.__players[playerToCheck],str)
                else:
                    output=-1
            elif len(str)==2:
                if str[0]['type']=='coin' and str[1]['type']=='coin' and str[0]['name']==str[1]['name'] and str[0]['name']!='gold':
                    output=moveTakeTwoCoinsCheck(self.__board.getCoins(),self.__players[playerToCheck].getPocket(),str)
                elif str[0]['type']=='coin' and str[0]['name']=='gold' and str[1]['type']=='card':
                    output=moveReservationCardCheck(self.__board,self.__players[playerToCheck],str)
                else:
                    output=-1
            elif len(str)==3:
                if str[0]['type']=='coin' and str[1]['type']=='coin' and str[2]['type']=='coin' and str[0]['name']!=str[1]['name'] and str[0]['name']!=str[2]['name'] and str[2]['name']!=str[1]['name']and str[0]['name']!='gold'and str[1]['name']!='gold'and str[2]['name']!='gold':
                    output=moveTakeCoinCheck(self.__board.getCoins(),self.__players[playerToCheck].getPocket(),str)
            else:
                raise Exception(f"Zła ilość poleceń\n{str}")
            return output
        def getRound(self):
            return self.__round
    def __init__(self):
        if not Game.__instance:
            Game.__instance=Game.__Game()
    def getBoard(self):
        return Game.__instance.getBoard()
    def move(self,str):
        Game.__instance.move(str)
    def moveCheck(self,move,player=None):
        return Game.__instance.moveCheck(move,player)
    def setup(self):
        Game.__instance.setup()
    def getPlayer(self,str):
        return Game.__instance.getPlayer(str)
    def getRound(self):
        return Game.__instance.getRound()
    def destroy(self):
        Game.__instance=None
    def runBetweenIA(self,first,second,iteration):
        pom=Game.__Game()
        return pom.runBetweenIA(first,second,iteration)
def moveByGoldenCard(board,player,move):
    cardWantToTake = player.getCardsByType('gold')[move[0]['index']]
    cardWantToTakeCoast = cardWantToTake.getCoasts()
    playerCoins = player.getPocket()
    neededResources = {}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        neededResources[i] = cardWantToTakeCoast.takeCoinByType(i).getCount()
        # tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(player.getCardsByType(i)) + playerCoins.takeCoinByType(i).getCount()) - neededResources[i] < 0:
            #print("nie możesz kupić karty")
            return -1
    #print("Możesz kupić kartę")
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        # tu trzeba będzie odjąć karty
        neededResources[i] -= len(player.getCardsByType(i))
        if neededResources[i] > 0:
            playerCoins.takeCoinByType(i).changeCount((-1) * neededResources[i])
            board.getCoins().takeCoinByType(i).changeCount(neededResources[i])
    player.getCardsByType('gold').remove(cardWantToTake)
    player.getPocket().takeCoinByType('gold').changeCount(-1)
    board.getCoins().takeCoinByType('gold').changeCount(1)
    player.addCard(cardWantToTake)
    player.addVicotorypoints(cardWantToTake.getVictoryPoints())
    return 1
def moveByGoldenCardCheck(board,player,move):
    if (len(player.getCardsByType('gold'))-1<move[0]['index'] or len(player.getCardsByType('gold'))<1):
        return -1
    cardWantToTake = player.getCardsByType('gold')[move[0]['index']]
    cardWantToTakeCoast = cardWantToTake.getCoasts()
    playerCoins = player.getPocket()
    neededResources = {}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        neededResources[i] = cardWantToTakeCoast.takeCoinByType(i).getCount()
        # tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(player.getCardsByType(i)) + playerCoins.takeCoinByType(i).getCount()) - neededResources[i] < 0:
            #print("nie możesz kupić karty")
            return -1
    return 1
def moveReservationCard(board,player,move):
    if player.getPocket().coinsCount()+1>15:
        return -1
    if board.getCoins().takeCoinByType('gold').getCount()==0:
        return -1
    if len(player.getCardsByType('gold'))==3:
        return -1
    cardWantToReserv=board.getCard(move[1]['y'],move[1]['x']-1)
    player.addCardToReservation(cardWantToReserv)
    player.getPocket().takeCoinByType('gold').changeCount(1)
    board.getCoins().takeCoinByType('gold').changeCount(-1)
    board.removeCard(cardWantToReserv)
    board.updateCardsAndLords()
    return 1
def moveReservationCardCheck(board,player,move):
    if player.getPocket().coinsCount()+1>15:
        return -1
    if board.getCoins().takeCoinByType('gold').getCount()==0:
        return -1
    if len(player.getCardsByType('gold'))==3:
        return -1
    return 1

def moveTakeLord(board,player,move):
    lord=board.getLordById(move[0]['number'])
    lordCoasts=lord.getCoasts()
    playerCards=player.getCards()
    for i in lordCoasts:
        if i['count']>len(playerCards[i['name']]):
            return -1
    player.addLord(lord)
    board.removeLord(lord)
    board.updateCardsAndLords()
    player.addVicotorypoints(lord.getvictoryPoints())
    return 1
def moveTakeLordCheck(board,player,move):
    lord=board.getLordById(move[0]['number'])
    lordCoasts=lord.getCoasts()
    playerCards=player.getCards()
    for i in lordCoasts:
        if i['count']>len(playerCards[i['name']]):
            return -1
    return 1
def moveTakeTwoCoins(boardPocket,playerPocket,moves):
    if boardPocket.takeCoinByType(moves[0]['name']).getCount()<4:
        return -1
    if playerPocket.coinsCount()+len(moves)>15:
        return -1
    boardPocket.takeCoinByType(moves[0]['name']).changeCount(-2)
    playerPocket.takeCoinByType(moves[0]['name']).changeCount(2)
    return 1
def moveTakeTwoCoinsCheck(boardPocket,playerPocket,moves):
    if boardPocket.takeCoinByType(moves[0]['name']).getCount()<4:
        return -1
    if playerPocket.coinsCount()+len(moves)>15:
        return -1
    return 1
def moveTakeCoin(boardPocket, playerPocket, moves):
    if playerPocket.coinsCount()+len(moves)>15:
        return -1
    for i in moves:
        for j in boardPocket.getAllCoins():
            if i['name']==j.getType():
                if j.getCount()==0:
                    return -1
                else:
                    break
    for i in moves:
        for j in boardPocket.getAllCoins():
            if i['name']==j.getType():
                playerPocket.takeCoinByType(i['name']).changeCount(1)
                j.changeCount(-1)
                break
    return 1
def moveTakeCoinCheck(boardPocket, playerPocket, moves):
    if playerPocket.coinsCount()+len(moves)>15:
        return -1
    for i in moves:
        for j in boardPocket.getAllCoins():
            if i['name']==j.getType():
                if j.getCount()==0:
                    return -1
                else:
                    break
    return 1
def moveTakeCard(board,player,move):
    cardWantToTake=board.getCard(move[0]['y'],move[0]['x']-1)
    cardWantToTakeCoast=cardWantToTake.getCoasts()
    playerCoins=player.getPocket()
    neededResources={}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        neededResources[i]=cardWantToTakeCoast.takeCoinByType(i).getCount()
        #tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(player.getCardsByType(i))+playerCoins.takeCoinByType(i).getCount())-neededResources[i]<0:
            #print("nie możesz kupić karty")
            return -1
    #print("Możesz kupić kartę")
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        #tu trzeba będzie odjąć karty
        neededResources[i]-=len(player.getCardsByType(i))
        if neededResources[i]>0:
            playerCoins.takeCoinByType(i).changeCount((-1)*neededResources[i])
            board.getCoins().takeCoinByType(i).changeCount(neededResources[i])
    board.removeCard(cardWantToTake)
    board.updateCardsAndLords()
    player.addCard(cardWantToTake)
    player.addVicotorypoints(cardWantToTake.getVictoryPoints())
    return 1
def moveTakeCardCheck(board,player,move):
    cardWantToTake=board.getCard(move[0]['y'],move[0]['x']-1)
    cardWantToTakeCoast=cardWantToTake.getCoasts()
    playerCoins=player.getPocket()
    neededResources={}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        neededResources[i]=cardWantToTakeCoast.takeCoinByType(i).getCount()
        #tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(player.getCardsByType(i))+playerCoins.takeCoinByType(i).getCount())-neededResources[i]<0:
            #print("nie możesz kupić karty")
            return -1
    return 1