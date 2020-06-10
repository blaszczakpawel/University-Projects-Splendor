import tkinter as tk

CRYSTALS = ['ruby','emerald','diamond','onyx','sapphire']

class Lord:
    def __init__(self, victory_points, photo, coasts):
        self.__vicotry_points = victory_points
        self.__photo = photo
        self.__coasts = coasts
        self.__image = None
        self.__small_image = None
    def __get_image_path(self):
        return self.__photo
    def get_image(self):
        if self.__image is None:
            self.__image = tk.PhotoImage(file=self.__get_image_path())
        return self.__image
    def get_small_image(self):
        if self.__small_image is None:
            self.__small_image = tk.PhotoImage(file=self.__get_image_path()).subsample(2)
        return self.__small_image
    def get_coasts(self):
        return self.__coasts
    def get_victory_points(self):
        return self.__vicotry_points
    def get_lords_stats_for_conector(self):
        output = []
        output.append(self.get_victory_points())
        for i in CRYSTALS:
            if i in self.__coasts:
                output.append(self.__coasts[i])
            else:
                output.append(0)
        return output
