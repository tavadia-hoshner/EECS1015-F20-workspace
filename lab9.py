# Lab 9 - Main
# Class:- EECS 1015
# Author:- Hoshner Tavadia
# Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
# Student Id:- 217828567

from MinMaxList import MinMaxList
from random import randint

# Main function is given.
def main():
    aList = MinMaxList([10, 11, 99, 1, 34, 88])

    print("--Insert Item--")
    for i in range(30):
        x = randint(1, 100)
        aList.insertItem(x, True)

    print("--Get Min--")
    for i in range(10):
        print("Min item = %d " % aList.getMin())
        aList.printList()

    print("--Get Max--")
    for i in range(10):
        print("Max item = %d " % aList.getMax())
        aList.printList()

if __name__ == "__main__":
    main()
