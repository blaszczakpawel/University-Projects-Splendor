class Person:
    def __init__(self, number, path):
        self.__number = number
        self.__count_of_fights = 0
        self.__points = 0
        self.__path = path+"_"+str(self.__number)
    def __str__(self):
        return f"Number: {self.__number} Fights: {self.__count_of_fights} Points: {self.__points}"
    def get_number(self):
        return self.__number
    def get_count_of_fights(self):
        return self.__count_of_fights
    def add_fight(self):
        self.__count_of_fights += 1
    def add_points(self, points):
        self.__points += points
    def get_points(self):
        return self.__points
    def setup_fight(self):
        self.__count_of_fights = 0
    def setup_points(self):
        self.__points=0
    def mutation(self):
        pass
    def get_to_fight(self):
        pass
    def get_path(self):
        return self.__path