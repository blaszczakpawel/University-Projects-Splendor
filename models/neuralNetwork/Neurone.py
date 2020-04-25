import math
from random import randint
from decimal import Decimal
class Neurone:
    def __init__(self,**kwargs):
        self.__size=None
        self.__weights=[]
        self.__bias=None
        self.__b=None
        self.__lastInput=None
        if "size" in kwargs and "weights" in kwargs:
            raise Exception("You cannot run Neurone with size ane weights arguments")
        for k,v in kwargs.items():
            if k=="size":
                self.__size=v
            elif k=="bias":
                self.__bias=v
            elif k=="weights":
                self.__weights=v
                self.__size=len(self.__weights)
            elif k=="b":
                if v>0:
                    self.__b=v
                else:
                    raise Exception("b must be larger then 0")
            elif k=="teaching":
                if v==True:
                    self.__lastInput=[]
                elif v==False:
                    self.__lastInput=None
                else:
                    raise Exception("Bad value for teaching variable")
            else:
                raise Exception("This argument does not exist")
    def __str__(self):
        return f"Funkcja przejścia:[b:{self.__b}], bias:{self.__bias}  weights:{self.__size}:{self.__weights} ]"
    def __calculateWeightsValue(self,array):
        self.__lastInput=array;
        count=self.__bias
        for i in range(len(self.__weights)):
            count+=self.__weights[i]*array[i]
        return count
    def __transitionFuction(self,value):
        """
        pom=(value-self.__b)/(2*(self.__c**2))
        pom2=pom*((value-self.__b))
        value=((self.__a*math.e)**(-pom2))
        """
        #return 1/(1+(math.e**(-(self.__b*value))))
        #return float(Decimal(1)/(Decimal(1)+(Decimal(math.e)**(Decimal(-1)*Decimal(self.__b)*Decimal(value)))))
        """
        if value>(math.pi/2):
            return 1
        if value<(math.pi/2):
            return 0
        return (math.sin(value)/2)+0.5
        """

        return (math.tanh(value)+1)/2
        #return 1 / (1 + math.exp(-value))
    def run(self,array):
        for i in [self.__b,self.__size,self.__bias]:
            if i==None:
                raise Exception("Neuron is not ready for work")
        if type(array)!=type([]):
            raise Exception("Argument must be array")
        if len(array)!=self.__size:
            raise Exception("weights array and values array isnt same length")
        return self.__transitionFuction(self.__calculateWeightsValue(array))
    def getSize(self):
        return self.__size
    def randomGenerate(self):
        if self.__b == None:
            #self.__b=(randint(1,10000)/10000)
            self.__b = 2
        if self.__bias==None:
            self.__bias=(randint(-300,300)/25)
        if self.__size==None:
            self.__size=randint(100,1000)
        if len(self.__weights)==0:
            for i in range(self.__size):
                self.__weights.append(randint(-100000,100000)/10000)
    def transformToObject(self):
        output={}
        output['przejscie'] = self.__b
        output['neurone']={}
        output['neurone']['bias']=self.__bias
        output['neurone']['weights']=self.__weights
        return output
    def transformFromObject(self,object):
        self.__b = object['przejscie']
        self.__bias = object['neurone']['bias']
        self.__weights = object['neurone']['weights']
        self.__size=len(self.__weights)
    def __mul__(self, other):
        if type(other)!=type(self):
            raise Exception("You cannot multiplay")
        if self.getSize()!=other.getSize():
            raise Exception("Size arent similar")
        array=[]
        for i in range(self.__size):
            array.append((self.__weights[i]+other.__weights[i])/2)
        return Neurone(weights=array,a=((self.__a+other.__a)/2),b=((self.__b+other.__b)/2),c=((self.__c+other.__c)/2),bias=((self.__bias+other.__bias)/2))
    def teaching(self, teachingRatio, teachingVariable):
        if self.__lastInput==None:
            raise Exception("I cant teach")
        countOfIncrise=0
        countOfDecrise=0
        arrayOfWeightsChange=[]
        for i in range(self.__size):
            pom=(self.__weights[i]*self.__lastInput[i])
            if pom>0 and teachingVariable>0:
                countOfIncrise+=1
                arrayOfWeightsChange.append((teachingVariable * teachingRatio * math.fabs(self.__weights[i])))
            elif pom>0 and teachingVariable<0:
                countOfDecrise+=1
                arrayOfWeightsChange.append((teachingVariable * teachingRatio * math.fabs(self.__weights[i])))
            elif pom < 0 and teachingVariable > 0:
                countOfIncrise += 1
                arrayOfWeightsChange.append((teachingVariable * teachingRatio * math.fabs(self.__weights[i])))
            elif pom < 0 and teachingVariable < 0:
                countOfDecrise += 1
                arrayOfWeightsChange.append((teachingVariable * teachingRatio * math.fabs(self.__weights[i])))
            else:
                arrayOfWeightsChange.append(0)
        if countOfDecrise > 4 * countOfIncrise or countOfIncrise > 4 * countOfDecrise:
            self.__bias += teachingVariable * teachingRatio
        else:
            for i in range(self.__size):
                self.__weights[i] += arrayOfWeightsChange[i]
                arrayOfWeightsChange[i]*=0.92
        return arrayOfWeightsChange
    def teachingSwitch(self):
        if self.__lastInput==None:
            self.__lastInput=[]
        self.__lastInput=None


