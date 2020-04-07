import tkinter as tk
class Lord:
    def __init__(self,victoryPoints,photo,coasts):
        self.__vicotryPoints=victoryPoints
        self.__photo=photo
        self.__coasts=coasts
        self.__image=None
    def __getImagePath(self):
        return self.__photo
    def getImage(self):
        if self.__image==None:
            self.__image=tk.PhotoImage(file=self.__getImagePath())
        return self.__image
