import tkinter as tk
class Frame:
    def __init__(self,root):
        self.__frame=tk.Frame(root)
        self.__widgets=[]
    def getFrame(self):
        return self.__frame
    def addToWidgetes(self,new):
        if new not in self.__widgets:
            self.__widgets.append(new)
    def update(self):
        raise NotImplemented()