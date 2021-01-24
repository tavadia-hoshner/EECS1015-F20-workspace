# Lab 9 - MinMaxList
# Class:- EECS 1015
# Author:- Hoshner Tavadia
# Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
# Student Id:- 217828567


class MinMaxList:

    def __init__(self, initializeList):
        self.listData = initializeList
        self.listData.sort()

    def insertItem(self, item, printResult=True):
        listlen = len(self.listData)
        self.item = item
        self.pos = 0
        if listlen == 0:
            self.listData.append(self.item)
        elif item >= self.listData[listlen-1]:
            self.listData.append(self.item)
            self.pos = listlen
        else:
            leng = len(self.listData)
            for i in range(leng):
                if self.listData[i] >= item:
                    self.pos = i
                    break
            self.listData.insert(self.pos, item)
        if printResult:
            print("item (%d) inserted at location %d" % (item, self.pos))
            print(self.listData)

    def getMin(self):
        if len(self.listData) == 0:
            return None
        result = self.listData[0]
        del self.listData[0]
        return result

    def getMax(self):
        if len(self.listData) == 0:
            return None
        result = self.listData[-1]
        del self.listData[-1]
        return result

    def printList(self):
        print(self.listData)
