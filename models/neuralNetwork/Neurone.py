import math
import random

GENERATE_TRANSITION_FUNCTION_B=2
GENERATE_BIAS_PROPERTIES=(-300,300)
GENERATE_BIAS_DIVIDER=25
GENERATE_SIZE_PROPERTIES=(100,1000)
GENERATE_WEIGHTS_PROPERTIES=(-100000,100000)
GENERATE_WEIGHTS_DIVIDER=5000

TEACHING_NON_ZERO_VARIABLE=1
TEACHING_PROPORTION=4
TEACHING_LAYERS_PROPORTION=0.92

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
            self.__b = GENERATE_TRANSITION_FUNCTION_B
        if self.__bias==None:
            self.__bias=(random.randint(*GENERATE_BIAS_PROPERTIES)/GENERATE_BIAS_DIVIDER)
        if self.__size==None:
            self.__size=random.randint(*GENERATE_SIZE_PROPERTIES)
        if len(self.__weights)==0:
            for i in range(self.__size):
                self.__weights.append(random.randint(*GENERATE_WEIGHTS_PROPERTIES)/GENERATE_WEIGHTS_DIVIDER)
    def transformToObject(self):
        output={}
        output['przejscie'] = self.__b
        output['neurone']={}
        output['neurone']['bias']=self.__bias
        output['neurone']['weights']=self.__weights
        output['lastInput']=self.__lastInput
        return output
    def transformFromObject(self,object):
        self.__b = object['przejscie']
        self.__bias = object['neurone']['bias']
        self.__weights = object['neurone']['weights']
        self.__size=len(self.__weights)
        self.__lastInput=object['lastInput']
    def __mul__(self, other):
        if type(other)!=type(self):
            raise Exception("You cannot multiplay")
        if self.getSize()!=other.getSize():
            raise Exception("Size arent similar")
        array=[]
        for i in range(self.__size):
            array.append((self.__weights[i]+other.__weights[i])/2)
        return Neurone(weights=array,b=((self.__b+other.__b)/2),bias=((self.__bias+other.__bias)/2))
    def teaching(self, teachingRatio, teachingVariable):
        if self.__lastInput==None:
            raise Exception("I cant teach")
        countOfIncrise=0
        countOfDecrise=0
        arrayOfWeightsChange=[]
        for i in range(self.__size):
            weigth=self.__weights[i] if abs(self.__weights[i])>TEACHING_NON_ZERO_VARIABLE else (-1 if self.__weights[i]<0 else 1)
            #weigth=-1 if self.__weights[i]<0 else 1
            pom=(weigth*self.__lastInput[i])
            if pom>0 and teachingVariable>0:
                countOfIncrise+=1
                arrayOfWeightsChange.append((teachingVariable * teachingRatio * math.fabs(pom)))
            elif pom>0 and teachingVariable<0:
                countOfDecrise+=1
                arrayOfWeightsChange.append((teachingVariable * teachingRatio * math.fabs(pom)))
            elif pom < 0 and teachingVariable > 0:
                countOfIncrise += 1
                arrayOfWeightsChange.append((teachingVariable * teachingRatio * math.fabs(pom)))
            elif pom < 0 and teachingVariable < 0:
                countOfDecrise += 1
                arrayOfWeightsChange.append((teachingVariable * teachingRatio * math.fabs(pom)))
            else:
                arrayOfWeightsChange.append(0)
        if countOfDecrise > TEACHING_PROPORTION * countOfIncrise or countOfIncrise > TEACHING_PROPORTION * countOfDecrise:
            self.__bias += teachingVariable * teachingRatio
        else:
            for i in range(self.__size):
                self.__weights[i] += arrayOfWeightsChange[i]
                arrayOfWeightsChange[i]*=TEACHING_LAYERS_PROPORTION
        return arrayOfWeightsChange
    def teachingSwitch(self):
        if self.__lastInput==None:
            self.__lastInput=[]
        self.__lastInput=None
    def setBias(self,bias):
        self.__bias=bias
    def getWeightsSize(self):
        return len(self.__weights)
    def setWeight(self,index,weight):
        self.__weights[index]=weight



