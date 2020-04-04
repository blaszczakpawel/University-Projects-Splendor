import tkinter as tk
import models.game.Game as game
import models.GUI.Frame as Frame
import models.GUI.Board as GUIBoard
import models.game.Board as GameBoard
import models.GUI.AcceptionBoard as AB
import models.GUI.Player as P
class GUI:
    def __init__(self,game):
        self.__game=game
        self.__window=self.__setWindow()
        self.__mainBoar=self.__setMainBoard(self.__window)
    def __setWindow(self):
        window=tk.Tk()
        window.geometry("900x900")
        window.title("Splendor")
        return window
    def __setMainBoard(self,root):
        self.__frames={}
        #['playerOne',1,4,'player']['playerTwo',1,2,'player']['main',1,1,'main']
        for i in [['accept','accept',2,3,170,0],['board','board',1,3,0,0],['player','one',1,4,70,40],['player','two',1,2,70,40]]:
            if i[0]=='board':
                self.__frames[i[1]]=GUIBoard.Board(root,self.__game.getBoard())
            elif i[0]=='accept':
                self.__frames[i[1]]=AB.AcceptionBoard(root)
            elif i[0]=='player':
                self.__frames[i[1]] = P.Player(root,self.__game.getPlayer(i[1]))
            self.__frames[i[1]].getFrame().grid(column=i[2], row=i[3], padx=i[4], pady=i[5])
    def refresh(self):
        for i in self.__frames:
            self.__frames[i].refresh()


