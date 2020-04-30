class Person:
    def __init__(self,number):
        self.__obj=None
        self.__number=number
        self.__countOfFights=0
        self.__points=0
    def __str__(self):
        return f"Number: {self.__number} Fights: {self.__countOfFights} Points: {self.__points}"
    def getCountOfFights(self):
        return self.__countOfFights
    def addFight(self):
        self.__countOfFights+=1
    def addPoints(self,points):
        self.__points+=points
    def getPoints(self):
        return self.__points
    def mutation(self):
        pass
    def copulate(self,other,number):
        pom = Person(number)
        return pom