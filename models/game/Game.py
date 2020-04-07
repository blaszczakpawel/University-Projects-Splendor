import models.game.Board as B
import models.game.Player as P
import models.simple.Pocket as PC
import models.simple.Coin as C
import models.GUI.GUI as G
import tkinter as tk
class Game:
    __instance=None
    class __Game:
        def __init__(self):
            self.__players={}
            self.__actualPlayer = "one"
            self.__board = B.Board()
            self.__pocket = PC.Pocket()
            for i in ['one','two']:
                self.__players[i]=P.Player(i)
        def getPlayer(self,str):
            return self.__players[str]
        def getBoard(self):
            return self.__board
        def setup(self):
            self.__gui = G.GUI(self)
            tk.mainloop()
        def move(self,str):
            output=0
            if len(str)==1:
                if str[0]['type']=='lord':
                    raise Exception("Jeszcze nie implementowane")
                elif str[0]['type']=='card':
                    raise Exception("Jescze nie implementowane")
                else:
                    raise Exception("Błąd")
            elif len(str)==2:
                raise Exception("Jescze nie implementowane")
            elif len(str)==3:
                if str[0]['type']=='coin' and str[1]['type']=='coin' and str[2]['type']=='coin' and str[0]['name']!=str[1]['name'] and str[0]['name']!=str[2]['name'] and str[2]['name']!=str[1]['name']:
                    output=moveTakeCoin(self.__board.getCoins(),self.__players[self.__actualPlayer].getPocket(),str)
            else:
                raise Exception("Zła ilość poleceń")
            #zamieniam graczy
            if self.__actualPlayer=="one":
                self.__actualPlayer="two"
            else:
                self.__actualPlayer="one"
            self.__gui.refresh()
    def __init__(self):
        if not Game.__instance:
            Game.__instance=Game.__Game()
    def getBoard(self):
        return Game.__instance.getBoard()
    def move(self,str):
        Game.__instance.move(str)
    def setup(self):
        Game.__instance.setup()
    def getPlayer(self,str):
        Game.__getPlayer(str)

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

