class CrystalCard:
    def __init__(self,XMLtree):
        self.__setVictoryPoints(int(XMLtree.find('victoryPoints').text))
        #print(self.getVictoryPoints())

        self.__setPhotoPath(XMLtree.find('photo').text)
        #print(self.getPhotoPath())

        costs={}
        for cost in XMLtree.iter('cost'):
            costs[cost.attrib['name']]=int(cost.text)
        self.__setCosts(costs)
        #print(self.getCosts())

        earnings = {}
        for earning in XMLtree.iter('earning'):
            earnings[earning.attrib['name']]=int(earning.text)
        self.__setEarnings(earnings)
        #print(self.getEarnings())

    def getVictoryPoints(self):
        return self.__victoryPoints
    def getCosts(self):
        return self.__costs
    def getEarnings(self):
        return self.__earnings
    def getPhotoPath(self):
        return self.__photoPath
    def __setVictoryPoints(self,victoryPoints):
        if(type(victoryPoints)!=int):
            raise Exception("bad format of vicotryPoints variable" + " " + str(type(victoryPoints)))
        self.__victoryPoints=victoryPoints
    def __setCosts(self,costs):
        if(type(costs)!=dict):
            raise Exception("bad format of costs variable")
        self.__costs=costs
    def __setEarnings(self,earnings):
        if(type(earnings)!=dict):
            raise Exception("bad format of earnings variable")
        self.__earnings=earnings
    def __setPhotoPath(self,photoPath):
        if(type(photoPath)!=str):
            raise Exception("bad format of photoPath")
        self.__photoPath=photoPath
    

