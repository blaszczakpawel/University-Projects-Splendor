import models.game.Board as B
import models.game.Player as P
import models.simple.Pocket as PC
import tkinter as tk
class Game:
    def __init__(self):
        self.__players=[]
        for i in ['one','two']:
            self.__players.append(P.Player(i))
        self.__board=B.Board()
        self.__pocket=PC.Pocket()
    def getBoard(self):
        return self.__board
