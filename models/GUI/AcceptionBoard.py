import models.GUI.Frame as F
import tkinter as tk
from functools import partial
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
            label=tk.Label(self.__board.getFrame(),textvariable=self.__str)
            label.grid(column=1,row=1)
            self.__board.addToWidgetes(label)
            button=tk.Button(self.__board.getFrame(),text="Wyczyść ruch",command=self.clear)
            button2=tk.Button(self.__board.getFrame(),text="Akceptuj ruch",command=self.acceptMove)
            button.grid(column=1,row=2)
            button2.grid(column=1,row=3)
            self.__board.addToWidgetes(button2)
            self.__board.addToWidgetes(button)
        def getFrame(self):
            return self.__board.getFrame()
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