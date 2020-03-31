import tkinter as tk
import models.game.Game as game
import models.GUI.Frame as Frame
import models.GUI.Board as GUIBoard
import models.game.Board as GameBoard
class GUI:
    def __init__(self):
        self.__game=game.Game()
        self.__window=self.__setWindow()
        self.__mainBoar=self.__setMainBoard(self.__window)
        tk.mainloop()
    def __setWindow(self):
        window=tk.Tk()
        window.geometry("900x900")
        window.title("Splendor")
        return window
    def __setMainBoard(self,root):
        self.__frames={}
        for i in [['playerOne',1,4,'player'],['playerTwo',1,2,'player'],['board',1,3,'board'],['coins',2,3,'coins'],['main',1,1,'main']]:
            if i[3]=='board':
                self.__frames[i[0]]=GUIBoard.Board(root,self.__game.getBoard())
                self.__frames[i[0]].getFrame().grid(column=i[1],row=i[2])
    def test(self):
        print("działa ładnie git XD")