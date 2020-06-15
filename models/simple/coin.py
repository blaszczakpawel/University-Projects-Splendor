import tkinter as tk
class Coin:
    __images = {}
    def __init__(self, type, count):
        self.__type = type
        self.__count = int(count)
    def get_type(self):
        return self.__type
    def get_count(self):
        return self.__count
    def get_coin(self, count):
        if self.__count-count >= 0:
            return count
        return 0
    def change_count(self, count):
        self.__count += count
    def get_image(self):
        if self.get_type() not in Coin.__images.keys():
            Coin.__images[self.get_type()] = tk.PhotoImage(file=f"photos/Coins/{self.get_type()}.png").subsample(2)
        return Coin.__images[self.get_type()]

