import models.game.Board as B
import models.game.Player as P
import models.simple.Pocket as PC
import tkinter as tk
class Game:
<<<<<<< Updated upstream
=======
    __instance=None
    class __Game:
        def __init__(self):
            self.__players={}
            self.__actualPlayer = "one"
            self.__board = B.Board()
            self.__round=0
            for i in ['one','two']:
                self.__players[i]=P.Player(i)
        def getPlayer(self,str):
            if str=='actual':
                return self.__players[self.__actualPlayer]
            return self.__players[str]
        def getBoard(self):
            return self.__board
        def setup(self):
            self.__gui = G.GUI(self)
            tk.mainloop()
        def move(self,str):
            print(str)
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
                if str[0]['type']=='coin' and str[1]['type']=='coin' and str[0]['name']==str[1]['name']:
                    output=moveTakeTwoCoins(self.__board.getCoins(),self.__players[self.__actualPlayer].getPocket(),str)
                elif str[0]['type']=='coin' and str[0]['name']=='gold' and str[1]['type']=='card':
                    output=moveReservationCard(self.__board,self.__players[self.__actualPlayer],str)
                else:
                    output=-1
            elif len(str)==3:
                if str[0]['type']=='coin' and str[1]['type']=='coin' and str[2]['type']=='coin' and str[0]['name']!=str[1]['name'] and str[0]['name']!=str[2]['name'] and str[2]['name']!=str[1]['name']:
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
                    if self.__players['one'].getVictoryPoints()>=15 or self.__players['two'].getVictoryPoints()>=15:
                        if self.__players['one'].getVictoryPoints()>self.__players['two'].getVictoryPoints():
                            print("Wygrał gracz one")
                        if self.__players['one'].getVictoryPoints()<self.__players['two'].getVictoryPoints():
                            print("Wygrał gracz two")
            self.__gui.refresh()
>>>>>>> Stashed changes
    def __init__(self):
        self.__players=[]
        for i in ['one','two']:
            self.__players.append(P.Player(i))
        self.__board=B.Board()
        self.__pocket=PC.Pocket()
    def getBoard(self):
<<<<<<< Updated upstream
        return self.__board
=======
        return Game.__instance.getBoard()
    def move(self,str):
        Game.__instance.move(str)
    def setup(self):
        Game.__instance.setup()
    def getPlayer(self,str):
        return Game.__instance.getPlayer(str)
def moveByGoldenCard(board,player,move):
    cardWantToTake = player.getCardsByType('gold')[move[0]['index']]
    cardWantToTakeCoast = cardWantToTake.getCoasts()
    playerCoins = player.getPocket()
    neededResources = {}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        neededResources[i] = cardWantToTakeCoast.takeCoinByType(i).getCount()
        # tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(player.getCardsByType(i)) + playerCoins.takeCoinByType(i).getCount()) - neededResources[i] < 0:
            print("nie możesz kupić karty")
            return -1
    print("Możesz kupić kartę")
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
def moveReservationCard(board,player,move):
    if player.getPocket().coinsCount()+1>10:
        return -1
    if board.getCoins().takeCoinByType('gold')==0:
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
def moveTakeTwoCoins(boardPocket,playerPocket,moves):
    if boardPocket.takeCoinByType(moves[0]['name']).getCount()<4:
        return -1
    if playerPocket.coinsCount()+len(moves)>10:
        return -1
    boardPocket.takeCoinByType(moves[0]['name']).changeCount(-2)
    playerPocket.takeCoinByType(moves[0]['name']).changeCount(2)
    return 1
def moveTakeCoin(boardPocket, playerPocket, moves):
    if playerPocket.coinsCount()+len(moves)>10:
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
def moveTakeCard(board,player,move):
    cardWantToTake=board.getCard(move[0]['y'],move[0]['x']-1)
    cardWantToTakeCoast=cardWantToTake.getCoasts()
    playerCoins=player.getPocket()
    neededResources={}
    for i in ['diamond', 'emerald', 'sapphire', 'onyx', 'ruby']:
        neededResources[i]=cardWantToTakeCoast.takeCoinByType(i).getCount()
        #tu powinienem od neededResources odjąć ilość kart danego typu które posiadam
        if (len(player.getCardsByType(i))+playerCoins.takeCoinByType(i).getCount())-neededResources[i]<0:
            print("nie możesz kupić karty")
            return -1
    print("Możesz kupić kartę")
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



    




>>>>>>> Stashed changes
