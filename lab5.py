#Lab 5
#Class:- EECS 1015
#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
#Student Id:- 217828567

names = ("Masha", "Kevin", "Ruigang", "Vlad", "Ramesh", "Aditi", "Caroline", "Panos", "Chuck", "Grani", "Rutha", "Stan", "Qiong", "Alexi", "Carlos")
cities = ("Toronto", "Ottawa", "Hamilton")
testDict = {"Richard":"Toronto", "Jia-Tao":"Toronto", "Justin":"Ottawa", "Lars":"Ottawa"}

import random

def getRandomItem(lista):
    listalength = len(lista)
    randomno = random.randint(0,(listalength-1))
    item = lista[randomno]
    return item

def createNameDictionary():
    dict = {}
    for x in names:
        dict[x]=getRandomItem(cities)
    return dict

def fromCity(dict, str):
    lista = []
    for x in dict:
        if dict[x] == str:
            lista.append(x)
    return lista

def removePeopleFrom(dict, str):
    lista=[]
    for x in dict:
        if dict[x]==str:
            lista.append(x)
            #del dict[x]
    for x in lista:
        del dict[x]

def printNameDict(dict, tuplea):
    for x in tuplea:
        lista = []
        for y in dict:
            if dict[y] == x:
                lista.append(y)
        if len(lista)>0:
            print("People From "+str(x) +":")
            ctr = 1
            for z in lista:
                print(str(ctr)+". "+z)
                ctr= ctr+1
        else:
            print("People From " + str(x) +":")
            print("*None*")


def main():
    # part 1 (Function testing)
    print("\nPart 1 - Testing functions with `testDict' \n")
    print("Testing getRandomItem() function")
    randomitem = getRandomItem(cities)
    print(randomitem)
    print("Testing fromCity() function")
    fromtoronto = fromCity(testDict,"Toronto")
    print(fromtoronto)
    fromottawa = fromCity(testDict,"Ottawa")
    print(fromottawa)
    print("Testing printNameDict() function")
    printNameDict(testDict,("Toronto","Ottawa"))
    print("Testing removePeopleFrom() function")
    removePeopleFrom(testDict,"Ottawa")
    printNameDict(testDict, ("Toronto", "Ottawa"))

    # part 2 (Main program with generated Dictionary)
    print("\nPart 2 - Main\n")
    maindict = createNameDictionary()
    printNameDict(maindict,cities)
    print("Toronto List:")
    print(fromCity(maindict,"Toronto"))
    print("Ottawa List:")
    print(fromCity(maindict, "Ottawa"))
    print("Hamilton List:")
    print(fromCity(maindict, "Hamilton"))
    removePeopleFrom(maindict,"Hamilton")
    removePeopleFrom(maindict,"Toronto")
    printNameDict(maindict,cities)

main()
