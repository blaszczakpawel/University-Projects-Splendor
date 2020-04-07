import tkinter as tk
import models.game.Game as game
import models.GUI.Frame as Frame
import models.GUI.Board as GUIBoard
import models.game.Board as GameBoard
class GUI:
    def __init__(self):
        self.__game=game.Game()
        self.__window=self.__setWindow()
<<<<<<< Updated upstream
        self.__mainBoar=self.__setMainBoard(self.__window)
        tk.mainloop()
=======
        self.__mainBoard=self.__setMainBoard(self.__window)
>>>>>>> Stashed changes
    def __setWindow(self):
        window=tk.Tk()
        window.geometry("1200x700")
        window.title("Splendor")
        return window
    def __setMainBoard(self,root):
        self.__frames={}
<<<<<<< Updated upstream
        for i in [['playerOne',1,4,'player'],['playerTwo',1,2,'player'],['board',1,3,'board'],['coins',2,3,'coins'],['main',1,1,'main']]:
            if i[3]=='board':
                self.__frames[i[0]]=GUIBoard.Board(root,self.__game.getBoard())
                self.__frames[i[0]].getFrame().grid(column=i[1],row=i[2])
    def test(self):
        print("działa ładnie git XD")
=======
        #['playerOne',1,4,'player']['playerTwo',1,2,'player']['main',1,1,'main']
        self.__playersFrame = tk.Frame(root)
        self.__playersFrame.grid(column=1, row=1)
        for i in [['accept','accept',3,1,100,0],['board','board',2,1,0,0],['player','one',1,2,70,0],['player','two',1,1,70,40]]:
            if i[0]=='board':
                self.__frames[i[1]]=GUIBoard.Board(root,self.__game.getBoard())
            elif i[0]=='accept':
                self.__frames[i[1]]=AB.AcceptionBoard(root)
            elif i[0]=='player':
                self.__frames[i[1]] = P.Player(self.__playersFrame,self.__game.getPlayer(i[1]),self.__game.getBoard())
            self.__frames[i[1]].getFrame().grid(column=i[2], row=i[3], padx=i[4], pady=i[5])
    def refresh(self):
        for i in self.__frames:
            self.__frames[i].refresh()


>>>>>>> Stashed changes
