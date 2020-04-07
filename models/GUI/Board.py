import models.GUI.Frame as Frame
import tkinter as tk
class Board(Frame.Frame):
    def __init__(self,root,board):
        super().__init__(root)
        self.__images=[]
        self.__board=board
        self.__crystalCards={}
<<<<<<< Updated upstream
        for i in [['low',0]]:
            self.__crystalCards[i[0]]=[]
            for j in range(4):
                card=self.__board.getCrystalCard(i[1],j)
                self.__images.append(tk.PhotoImage(file=card.getImagePath()))
                button=tk.Button(self.getFrame(),image=self.__images[len(self.__images)-1])
                button.grid(column=j,row=i[1])
                self.addToWidgetes(button)
=======
        self.__coins={}
        self.__lords=[]
        for i in range(4):
            lord=self.__board.getCard(0,i)
            self.__lords.append(tk.Button(self.__cardBoardFrame.getFrame(), image=lord.getImage(), command=partial(self.__acceptionBoard.move, f"Lord z pozycji {i} ",{'type':"lord","number":i})))
            self.__lords[len(self.__lords)-1].grid(column=i, row=0,padx=10, pady=10)
            self.__cardBoardFrame.addToWidgetes(self.__lords[len(self.__lords)-1])
        for i in [['high',1],['medium',2],['low',3]]:
            self.__crystalCards[i[0]]=[]
            for j in range(4):
                card=self.__board.getCard(i[1],j)
                self.__crystalCards[i[0]].append(tk.Button(self.__cardBoardFrame.getFrame(),image=card.getImage(), command=partial(self.__acceptionBoard.move,f"Karta z pozycji (x,y)=({j+1} , {i[1]})",{'type':"card","x":j+1,'y':i[1]})))
                self.__crystalCards[i[0]][j].grid(column=j,row=i[1],padx=10, pady=8)
                self.__cardBoardFrame.addToWidgetes(self.__crystalCards[i[0]][j])
        for i in [[0,'diamond'],[1,'ruby'],[2,'onyx'],[3,'sapphire'],[4,'emerald'],[5,'gold']]:
            self.__coins[i[1]]=tk.Label(self.__cardCoinsFrame.getFrame(),text=str(self.__board.getCoinByType(i[1]).getCount()))
            button=tk.Button(self.__cardCoinsFrame.getFrame(),image=self.__board.getCoinByType(i[1]).getImage(),command=partial(self.__acceptionBoard.move,f"Moneta o nazwie {i[1]}",{'type':"coin","name":i[1]}))
            self.__coins[i[1]].grid(column=1,row=i[0])
            button.grid(column=0,row=i[0],padx=4, pady=4)
            self.__cardCoinsFrame.addToWidgetes(self.__coins[i[1]])
            self.__cardCoinsFrame.addToWidgetes(button)
    def getFrame(self):
        return self.__mainBoardFrame.getFrame()
    def refresh(self):
        print("odświerzam Board")
        for i in range(4):
            lord=self.__board.getCard(0,i)
            self.__lords[i].configure(image=lord.getImage())
        for i in ['diamond','ruby','onyx','sapphire','emerald','gold']:
            self.__coins[i].configure(text=str(self.__board.getCoinByType(i).getCount()))
        for i in [['high',1],['medium',2],['low',3]]:
            for j in range(4):
                card=self.__board.getCard(i[1],j)
                self.__crystalCards[i[0]][j].configure(image=card.getImage())





>>>>>>> Stashed changes


