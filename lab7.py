#Lab 7
#Class:- EECS 1015
#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
#Student Id:- 217828567

import pytest
from typing import List

# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:   # given
    myList.sort()

def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()

def getMinMax(myList: List[int], minormax: str) -> int:   # given -- but requires additional assert
    assert minormax.upper()=="MAX" or minormax.upper()=="MIN", "2nd argument must be 'Min' or 'Max' "
    assert len(myList)>0, "The List Provided Is Invalid Or Empty"
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result

# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()


#####
# WRITE YOUR TEST CASES BELOW HERE
#
######

def test_getMinMaxCase1():
    x = [50,5]
    initializeMinMaxList(x)
    result1 = getMinMax(x,"min")
    result2 = getMinMax(x,"max")
    assert result1==5,"Min should be 5"
    assert result2==50, "Max should be 50"

def test_getMinMaxCase2():
    x = [10]
    initializeMinMaxList(x)
    result1 = getMinMax(x, "min")
    insertItem(x,10)
    result2 = getMinMax(x,"max")
    assert result1 == 10, "Min should be 10"
    assert result2 == 10, "Max should be 10"

def test_getMinMaxCase3():
    x=[]
    initializeMinMaxList(x)
    insertItem(x,10)
    insertItem(x,20)
    result1 = getMinMax(x, "min")
    result2 = getMinMax(x, "max")
    assert result1 == 10, "Min should be 10"
    assert result2 == 20, "Max should be 20"

def test_getMinMaxRequestError():
    x=[7,2,4]
    initializeMinMaxList(x)
    with pytest.raises(AssertionError) as e:
        result = getMinMax(x, "MID")
    assert e.typename=="AssertionError", "Should Raise Assertion Error"

def test_getMinMaxEmptyError():
    x=[]
    initializeMinMaxList(x)
    with pytest.raises(AssertionError) as e:
        result = getMinMax(x, "max")
    assert e.typename=="AssertionError", "Should Raise Assertion Error"
