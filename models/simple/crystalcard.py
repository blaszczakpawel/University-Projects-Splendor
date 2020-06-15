import tkinter as tk

import models.simple.pocket as pocket
import models.simple.coin as coin

CRYSTALS = ['ruby','emerald','diamond','onyx','sapphire']

class CrystalCard:
    __back = None
    def __init__(self, victoryPoints, coasts, earnings, photo):
        self.__imagePath = photo
        self.__victoryPoints = int(victoryPoints)
        self.__coasts = pocket.Pocket()
        self.__earnings = pocket.Pocket()
        self.__image = None
        self.__smal_image = None
        for i in coasts:
            self.__coasts.push(coin.Coin(i['name'], int(i['count'])))
        for i in earnings:
            self.__earnings.push(coin.Coin(i['name'], int(i['count'])))
    def get_back(self):
        if CrystalCard.__back is None:
            CrystalCard.__back = tk.PhotoImage(file="photos\High\cardsBack.png").subsample(2)
        return CrystalCard.__back
    def get_image_path(self):
        return self.__imagePath
    def get_image(self):
        if self.__image is None:
            self.__image = tk.PhotoImage(file=self.get_image_path())
        return self.__image
    def get_small_image(self):
        if self.__smal_image is None:
            self.__smal_image = tk.PhotoImage(file=self.get_image_path()).subsample(2)
        return self.__smal_image
    def get_coasts(self):
        return self.__coasts
    def get_type(self):
        return self.__earnings.get_all_coins()[0].get_type()
    def get_victory_points(self):
        return self.__victoryPoints
    def get_stats_for_conector(self):
        output = []
        output.append(self.get_victory_points())
        for i in CRYSTALS:
            output.append(self.__coasts.take_coin_by_type(i).get_count())
        for i in CRYSTALS:
            output.append(self.__earnings.take_coin_by_type(i).get_count())
        return output



