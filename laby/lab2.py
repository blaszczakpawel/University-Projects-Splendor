import math as math
import random as rand
import time as tm
def czyPierwsza(liczba):
    for i in range(2,int(math.sqrt(liczba)+1)):
        if liczba%i==0:
            return "liczba nie jest pierwsza"
    else:
        return "liczba jest pierwsza"

def printLab(text,line=80):
    left=int((line-len(text))/2)
    text2=""
    for i in range(left):
        text2=text2+" "
    print(text2+text)

def trzecieZadanie(steps,fx,xStart=-1,XStop=1):
    dx=(XStop-xStart)/steps
    for i in range(steps):
        print(f"f({xStart})={fx(xStart)}")
        xStart+=dx
def k4():
    print(int(rand.random()*4+1))
def k8():
    print(int(rand.random()*8+1))
def k10():
    print(int(rand.random()*10+1))
def k20():
    print(int(rand.random()*20+1))
def getDice(str):
    k=str.find('k')
    count=int(str[:k])
    fun=str[k:]
    for i in range(count):
        exec(fun+"()")


def napisy(*args,**argv):
    list=[]
    max=0
    for i in args:
        list.append(i)
        if len(i)>max:
            max=len(i)
    for i in argv:
        a=i+": "+argv[i]
        list.append(a)
        if len(a)>max:
            max=len(a)
    max=max+6
    for i in list:
        printLab(i,max)
        tm.sleep(1)

#getDice('10k8')


#trzecieZadanie(1,lambda x:x**2,-1,10)


napisy("ten film był dobry","polecam graczy",autor="Ktos co sie nie chce przyznac",scenariusz="musial byc")


