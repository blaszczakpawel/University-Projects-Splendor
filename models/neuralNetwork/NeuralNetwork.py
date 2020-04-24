from models.neuralNetwork.HiddenLayer import HiddenLayer
from math import fabs
class NeuralNetwork:
    def __init__(self,**kwargs):
        self.__hiddenLayers=[]
        for k,v in kwargs.items():
            if k=='cfg':
                for i in range(1,len(v)):
                    self.__hiddenLayers.append(HiddenLayer(countOfNeurons=v[i],sizeOfInput=v[i-1]))
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
            a=HiddenLayer()
            a.transformFromObject(i)
            self.__hiddenLayers.append(a)


cel=[0.1,0.2,0.95,0.67,0.997,0.56,0.7,0.45,0.001,0.68,0.1,0.2,0.95,0.67,0.997,0.56,0.7,0.45,0.001,0.68]
pom=[(i/1000)**2 for i in range(200)]
a=NeuralNetwork(cfg=[200,210,220,210,180,20])
a.randomGenerate()
wynik=[]
for j in range(1000000000):
    wynik=a.run(pom)
    nauka=[]
    for i in range(len(cel)):
        if wynik[i]-cel[i]>0.6:
            nauka.append(-0.8)
        elif wynik[i]-cel[i]>0.4:
            nauka.append(-0.5)
        elif wynik[i]-cel[i]>0.2:
            nauka.append(-0.3)
        elif wynik[i]-cel[i]>0.001:
            nauka.append(-0.1)
        elif wynik[i]-cel[i]>0.0000001:
            nauka.append(-0.001)
        elif wynik[i]-cel[i]<0.6:
            nauka.append(0.8)
        elif wynik[i]-cel[i]<0.4:
            nauka.append(0.5)
        elif wynik[i]-cel[i]<0.2:
            nauka.append(0.3)
        elif wynik[i]-cel[i]<0.001:
            nauka.append(0.1)
        elif wynik[i]-cel[i]<0.0000001:
            nauka.append(0.001)
        else:
            nauka.append(0)
    a.teaching(1/1000,nauka)
    if j%1000==0:
        print(wynik)
        max=0
    for i in range(len(wynik)):
        if fabs(wynik[i] - cel[i])>max:
            max=fabs(wynik[i] - cel[i])
    if max<00.1:
        print("Skończone z max")
        break
print("Koniec")
for i in range(len(wynik)):
    print(fabs(wynik[i]-cel[i]),end=" ")
print("\n")
print(a)