import models.GUI.Frame as Frame
import tkinter as tk
import models.GUI.AcceptionBoard as AB
from functools import partial
class Board():
    def __init__(self,root,board):
        self.__acceptionBoard=AB.AcceptionBoard()
        self.__mainBoardFrame=Frame.Frame(root)
        self.__cardBoardFrame=Frame.Frame(self.__mainBoardFrame.getFrame())
        self.__cardBoardFrame.getFrame().grid(row=1,column=0)
        self.__cardCoinsFrame=Frame.Frame(self.__mainBoardFrame.getFrame())
        self.__cardCoinsFrame.getFrame().grid(row=1,column=1)
        self.__images=[]
        self.__board=board
        self.__crystalCards={}
        for i in range(4):
            lord=self.__board.getCard(0,i)
            self.__images.append(tk.PhotoImage(file=lord.getImagePath()))
            button = tk.Button(self.__cardBoardFrame.getFrame(), image=self.__images[len(self.__images) - 1], command=partial(self.__acceptionBoard.move, f"Lord z pozycji {i} ",{'type':"lord","number":i}))
            button.grid(column=i, row=0,padx=10, pady=10)
            self.__cardBoardFrame.addToWidgetes(button)
        for i in [['high',1],['medium',2],['low',3]]:
            self.__crystalCards[i[0]]=[]
            for j in range(4):
                card=self.__board.getCard(i[1],j)
                self.__images.append(tk.PhotoImage(file=card.getImagePath()))
                button=tk.Button(self.__cardBoardFrame.getFrame(),image=self.__images[len(self.__images)-1], command=partial(self.__acceptionBoard.move,f"Karta z pozycji (x,y)=({j+1} , {i[1]})",{'type':"card","x":j+1,'y':i[1]}))
                button.grid(column=j,row=i[1],padx=10, pady=8)
                self.__cardBoardFrame.addToWidgetes(button)
        for i in [[0,'diamond'],[1,'ruby'],[2,'onyx'],[3,'sapphire'],[4,'emerald'],[5,'gold']]:
            self.__images.append(tk.PhotoImage(file=f"photos/Coins/{i[1]}.png").subsample(2))
            count=self.__board.getCoinByType(i[1]).getCount()
            label=tk.Label(self.__cardCoinsFrame.getFrame(),text=str(count))
            button=tk.Button(self.__cardCoinsFrame.getFrame(),image=self.__images[len(self.__images)-1],command=partial(self.__acceptionBoard.move,f"Moneta o nazwie {i[1]}",{'type':"coin","name":i[1]}))
            label.grid(column=1,row=i[0])
            button.grid(column=0,row=i[0],padx=4, pady=4)
            self.__cardCoinsFrame.addToWidgetes(label)
            self.__cardCoinsFrame.addToWidgetes(button)
    def getFrame(self):
        return self.__mainBoardFrame.getFrame()


