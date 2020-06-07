import models.neuralNetwork.Neurone as Neurone
class HiddenLayer:
    def __init__(self,**kwargs):
        self.__sizeOfInput=None
        self.__countOfNeurons=None
        self.__arrayOfNeurons=[]
        for k,v in kwargs.items():
            if k=='sizeOfInput':
                self.__sizeOfInput=v
            elif k=="countOfNeurons":
                self.__countOfNeurons=v
            elif k=="arrayOfNeurons":
                self.__arrayOfNeurons=v
            else:
                raise Exception(f"Bad name of argument {k}")
    def randomGenerate(self):
        if self.__sizeOfInput==None or self.__countOfNeurons==None or len(self.__arrayOfNeurons)!=0:
            raise Exception("Hidden Layer is actualy generate")
        for i in range(self.__countOfNeurons):
            newNeurone=Neurone.Neurone(size=self.__sizeOfInput,teaching=True)
            newNeurone.randomGenerate()
            self.__arrayOfNeurons.append(newNeurone)
    def __str__(self):
        output= f"SOI:{self.__sizeOfInput} CON:{self.__countOfNeurons} Neurons:{self.__arrayOfNeurons[0].__str__()}"
        for i in range(len(self.__arrayOfNeurons)-1):
            output+=f";{self.__arrayOfNeurons[i+1].__str__()}"
        output+="]"
        return output
    def getNeuronByIndex(self,index):
        if index<0  or index>=len(self.__arrayOfNeurons):
            raise Exception(f"Index out of neurons range {index} from {len(self.__arrayOfNeurons)}")
        else:
            return self.__arrayOfNeurons[index]
    def run(self,arrayOfInput):
        arrayOfOuput=[]
        for i in self.__arrayOfNeurons:
            arrayOfOuput.append(i.run(arrayOfInput))
        return arrayOfOuput
    def __mul__(self, other):
        if self.__sizeOfInput != other.__sizeOfInput:
            raise Exception("size of input into layers arent similar")
        if self.__countOfNeurons != other.__countOfNeurons:
            raise Exception("count of neurons isnt similar")
        return HiddenLayer(countOfNeurons=self.__countOfNeurons,sizeOfInput=self.__sizeOfInput,arrayOfNeurons=[(self.getNeuronByIndex(i)*other.getNeuronByIndex(i)) for i in range(self.__countOfNeurons)])
    def transformToObject(self):
        obj={}
        obj['sizeOfInput']=self.__sizeOfInput
        obj['countOfNeurons']=self.__countOfNeurons
        obj['arrayOfNeurons']=[]
        for i in self.__arrayOfNeurons:
            obj['arrayOfNeurons'].append(i.transformToObject())
        return obj
    def transformFromObject(self,obj):
        if len(self.__arrayOfNeurons) !=0:
            raise Exception("You cannot create")
        self.__countOfNeurons=obj['countOfNeurons']
        self.__sizeOfInput=obj['sizeOfInput']
        self.__arrayOfNeurons=[]
        for i in obj['arrayOfNeurons']:
            a=Neurone.Neurone()
            a.transformFromObject(i)
            self.__arrayOfNeurons.append(a)
    def teaching(self, teachingRatio, teachingVariablesArray):
        arrayOfWeights=[0 for i in range(self.__sizeOfInput)]
        for i in range(self.__countOfNeurons):
            counter=0
            for j in self.__arrayOfNeurons[i].teaching(teachingRatio,teachingVariablesArray[i]):
                arrayOfWeights[counter]+=j
                counter+=1
        return arrayOfWeights
    def getSizeOfInput(self):
        return self.__sizeOfInput
    def getSizeOfNeurons(self):
        return self.__countOfNeurons



