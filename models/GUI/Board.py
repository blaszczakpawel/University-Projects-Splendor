import models.GUI.Frame as Frame
import tkinter as tk
class Board(Frame.Frame):
    def __init__(self,root,board):
        super().__init__(root)
        self.__images=[]
        self.__board=board
        self.__crystalCards={}
        for i in [['low',0]]:
            self.__crystalCards[i[0]]=[]
            for j in range(4):
                card=self.__board.getCrystalCard(i[1],j)
                self.__images.append(tk.PhotoImage(file=card.getImagePath()))
                button=tk.Button(self.getFrame(),image=self.__images[len(self.__images)-1])
                button.grid(column=j,row=i[1])
                self.addToWidgetes(button)


