import models.neuralNetwork.HiddenLayer as HL

class NeuralNetwork:
    def __init__(self,**kwargs):
        self.__hiddenLayers=[]
        for k,v in kwargs.items():
            if k=='cfg':
                for i in range(1,len(v)):
                    self.__hiddenLayers.append(HL.HiddenLayer(countOfNeurons=v[i],sizeOfInput=v[i-1]))
    def teaching(self, teachingRatio, teachingVariablesArray):
        pom = self.__hiddenLayers[len(self.__hiddenLayers)-1].teaching(teachingRatio,teachingVariablesArray)
        for i in range(len(self.__hiddenLayers)-2,0,-1):
            pom=self.__hiddenLayers[i].teaching(teachingRatio,pom)
    def randomGenerate(self):
        for i in self.__hiddenLayers:
            i.randomGenerate()
    def __str__(self):
        output=""
        for i in self.__hiddenLayers:
            output+=f"{i.__str__()}\n"
        return output
    def run(self,array):
        if len(array)!=self.__hiddenLayers[0].getSizeOfInput():
            raise Exception("Bad input size")
        pom=[i for i in array]
        for i in self.__hiddenLayers:
            pom=i.run(pom)
        return pom
    def transformToObject(self):
        obj={}
        obj['hiddenLayers']=[]
        for i in self.__hiddenLayers:
            obj['hiddenLayers'].append(i.transformToObject())
        return obj
    def transformFromObject(self,obj):
        if len(self.__hiddenLayers)!=0:
            raise Exception("Błąd w luj")
        for i in obj['hiddenLayers']:
            a=HL.HiddenLayer()
            a.transformFromObject(i)
            self.__hiddenLayers.append(a)
    def getHiddenLayer(self,num):
        return self.__hiddenLayers[num]
    def getHiddenLayersLen(self):
        return len(self.__hiddenLayers)
    def getCfg(self):
        cfg=[self.__hiddenLayers[0].getSizeOfInput()]
        for i in self.__hiddenLayers:
            cfg.append(i.getSizeOfNeurons())
        return cfg
    def __mul__(self, other):
        if self.getCfg()!=other.getCfg():
            raise Exception("Bad cfg")
        newNetwork=NeuralNetwork(cfg=self.getCfg())
        for i in range(len(newNetwork.__hiddenLayers)):
            newNetwork.__hiddenLayers[i]=self.__hiddenLayers[i]*other.__hiddenLayers[i]
        return newNetwork
