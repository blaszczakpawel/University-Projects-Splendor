import models.GUI.Frame as F
import tkinter as tk
import functools
import models.game.Game as G
class AcceptionBoard:
    __instance=None
    class __AB:
        def __init__(self,root):
            self.__cfg=[]
            self.__game=G.Game()
            self.__count=0
            self.__str=tk.StringVar()
            self.__text="Twój ruch to:\n"
            self.__str.set(self.__text)
            self.__board=F.Frame(root)
            self.__board.getFrame().grid(row=1,column=2)
            self.__goldenCards=[]
            label=tk.Label(self.__board.getFrame(),textvariable=self.__str)
            label.grid(column=1,row=1)
            self.__board.addToWidgetes(label)
            for i in range(3):
                self.__goldenCards.append(tk.Button(self.__board.getFrame(),command=functools.partial(self.buyGoldCard,i)))
            for i in [["Wyczyść ruch",self.clear,1,2],["Wykup kartę",self.printGoldenCards,1,3],["pass",self.pas,1,4],["Akceptuj ruch",self.acceptMove,1,5]]:
                button=tk.Button(self.__board.getFrame(),text=i[0],command=i[1])
                button.grid(column=i[2], row=i[3])
                self.__board.addToWidgetes(button)
        def refresh(self):
            self.clear()
            for i in range(3):
                self.__goldenCards[i].grid_remove()
        def printGoldenCards(self):
            counter=0
            for i in self.__game.getPlayer('actual').getCardsByType('gold'):
                self.__goldenCards[counter].configure(image=i.getSmallImage())
                self.__goldenCards[counter].grid(row=0,column=counter)
                counter+=1
        def buyGoldCard(self,index):
            self.move(f" wykupienie złotej karty o indeksie {index+1}", {"type": "byGoldenCard","index":index})
        def getFrame(self):
            return self.__board.getFrame()
        def pas(self):
           self.move(" odpuszczenie tej kolejki",{"type":"pass"})
        def clear(self):
            self.__text="Twój ruch\n"
            self.__str.set(self.__text)
            self.__count=0
            self.__cfg=[]
        def acceptMove(self):
            self.__game.move(self.__cfg)
        def move(self,str,cfg):
            self.__count+=1
            if self.__count<4:
                self.__text+=f"{str}\n"
                self.__str.set(self.__text)
                self.__cfg.append(cfg)
            else:
                self.__str.set("Nie za dużo tych ruchów?")
    def __init__(self,*args):
        if not AcceptionBoard.__instance:
            AcceptionBoard.__instance=AcceptionBoard.__AB(args[0])
    def getFrame(self):
        return AcceptionBoard.__instance.getFrame()
    def move(self,str,cfg):
        AcceptionBoard.__instance.move(str,cfg)
    def refresh(self):
        #print("Odświerzam Acception Board")
        self.__instance.refresh()
