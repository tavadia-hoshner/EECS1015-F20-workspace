#Lab 6
#Class:- EECS 1015
#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
#Student Id:- 217828567

# data for Task1
rList = [ [1, 10, 9, 4, 50],
          [3, 40, 99, 37, 5, 1],
          [8, 11, 10, 94],
          [100, 9, 2, 88, 44],
          [4, 9, 2, 19]]

# data for Task 2
encodedData1 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')], [(9, ' '), (3, '8'), (1, 'l')], [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')], [(6, ' '), (1, '.'), (8, '8'), (1, '.')], [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')], [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')], [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')], [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')], [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'), (1, "'")], [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'), (1, '-'), (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '), (1, 'm'), (1, 'h')]]
encodedData2 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')], [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')], [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'), (3, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'), (7, '.'), (7, ' '), (3, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'), (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'), (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'), (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')], [(52, '.')]]

# data for Task 3
stringData = "1 H Hydrogen,2 He Helium,3 Li Lithium,4 Be Beryllium,5 B Boron,6 C Carbon,7 N Nitrogen,8 O Oxygen,9 F Fluorine,10 Ne Neon,11 Na Sodium,12 Mg Magnesium,13 Al Aluminum,14 Si Silicon,15 P Phosphorus,16 S Sulfur,17 Cl Chlorine,18 Ar Argon,19 K Potassium,20 Ca Calcium,21 Sc Scandium,22 Ti Titanium,23 V Vanadium,24 Cr Chromium,25 Mn Manganese"

#TASK 1
def printRaggedList(list1):
    listlen = len(list1)
    for row in range(listlen):
        print(f"row {row} :",list1[row])

def sortRaggedList(list1):
    for row in list1:
        row.sort()


#TASK2
def decodeTupleList(list2):
    string = ""
    for row in list2:
        string = string + (str(row[1])*int(row[0]))
    return string

def printEncodedAsciiImage(list2):
    for row in list2:
        print(decodeTupleList(row))


#TASK3
def buildElementDictionary(string3):
    listofelements = string3.split(",")
    dict3 = {}
    for element in listofelements:
        elementlist = element.strip().split()
        name = elementlist[2]
        atomic_no = elementlist[0]
        sym = elementlist[1]
        dict3[sym] = [name,atomic_no]
    return dict3

def printElements(dict3):
    for symbol in dict3:
        print(f"{symbol} [{dict3[symbol][0]}] #{dict3[symbol][1]}")

def main():
    #TASK1
    print("Task 1 - Sorting and printing a ragged list\n")
    print("--List Before Sorting--")
    printRaggedList(rList)
    sortRaggedList(rList)
    print("--List After Sorting--")
    printRaggedList(rList)
    #TASK2
    print("\n\nTask 2 - Decoding Ascii Art")
    print("\nASCII Art 1")
    printEncodedAsciiImage(encodedData1)
    print("\nASCII Art 2")
    printEncodedAsciiImage(encodedData2)
    #TASK3
    print("\n\nTask 3 - Elements String to Dictionary")
    Elementdict = buildElementDictionary(stringData)
    print(Elementdict)
    print("----First 25 Elements----")
    printElements(Elementdict)
    input()

main()