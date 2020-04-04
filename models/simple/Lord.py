class Lord:
    def __init__(self,victoryPoints,photo,coasts):
        self.__vicotryPoints=victoryPoints
        self.__photo=photo
        self.__coasts=coasts
    def getImagePath(self):
        return self.__photo
