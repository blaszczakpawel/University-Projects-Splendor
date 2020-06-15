import tkinter as tk

class MyFrame:
    def __init__(self,root):
        self.__frame=tk.Frame(root)
        self.__widgets=[]
    def get_frame(self):
        return self.__frame
    def add_to_widgetes(self, new):
        if new not in self.__widgets:
            self.__widgets.append(new)
    def update(self):
        raise NotImplementedError