####################
# EECS1015 - York University
# Final Exam - final.py
#
# IMPORTANT - Please put your info below (and in Task0)
# Name: Hoshner Tavadia
# Student ID: 217828567
# email address: hoshnertavadia@gmail.com / htavadia@my.yorku.ca
#
#####################

from math import sqrt
import utilities as util
# you will need to add code to import utilities variables

# write your task0 here
def task0():
  print("--- Task 0 ---")
  print("FinalExam - EECS1015")
  print("Name - Hoshner Tavadia")
  print("Student ID - 217828567")
  print("Email - hoshnertavadia@gmail.com / htavadia@my.yorku.ca\n")
  pass

# write your task1 here
# you can modify task1()'s parameter list
def task1(lyrics):
  print("--- Task 1 - Word Frequency ---")
  lyrics = lyrics.lower()
  lyrics = lyrics.replace(",","")
  lyrics = lyrics.replace(".","")
  lyrics = lyrics.split()
  words = set(lyrics)
  count = []
  astr = []
  for x in words:
    ctr = 0
    for y in lyrics:
      if x == y:
        ctr += 1
    count.append(ctr)
  words = list(words)
  for x in count:
    astr.append("*"*x)
  for x in range(len(words)):
    print("%10s [%d] %s"%(words[x],count[x],astr[x]))
  print("\n")
  pass

# write your task2 here
# you can modify task2()'s parameter list
def task2(origd):
  print("--- Task 2 - Dictionary Inversion ---")
  dict = origd.copy()
  age = set([])
  new_dict = {}
  for x in dict:
    age.add(dict[x])
  for a in age:
    lista = []
    for x in dict:
      if dict[x]==a:
        lista.append(x)
    new_dict[a]=lista
  print(new_dict)
  for x in new_dict:
    print("Age",x)
    for n in new_dict[x]:
      print(" ",n)
  print("\n")
  pass

# write your task3 here
# you can modify task3()'s parameter list
def task3(lista):
  print("--- Task 3 - Poor Person's Graphics ---")
  while True:
    rad = int(input("Enter A Radius [1 to 9]:- "))
    assert (rad>=1 and rad<=9), "Radius must be between 1-9"
    for i in range(20):
      for j in range(20):
        x = i - 10
        y = j - 10
        if sqrt(x ** 2 + y ** 2) <= rad:
          lista[i][j] = "*"
        else:
          lista[i][j] = " "
    for x in lista:
      for y in x:
        print(y, end="")
      print()
    ta = input("Try Again [Y/N]? :-").upper()
    if ta =="Y":
      pass
    elif ta =="N":
      break
    else:
      print("Invalid Input, Proceeding To Task 4")
      break
  print("\n")
  pass

# write your task4 here
# you can modify task4()'s parameter list
def task4(numList):
  print("--- Task 4 - Robust Statistics Of Corrupted Data ---")
  obj1 = util.listStats(numList, 0)         # no corruption
  obj2 = util.listStats(numList, 15)        # 15% chance of corruptio
  obj3 = util.listStats(numList, 30)        # 30% chance of corruptio
  obj1.printStatistics()                    # print stats
  obj2.printStatistics()                    # print stats
  obj3.printStatistics()                    # print stats
  pass


def main():

  task0()
  task1(util.lyrics)       # pass variable lyrics from utilities.py
  task2(util.nameDict)       # pass variable nameDict from utilities.py
  task3(util.raster)       # pass variable raster from utilities.py
  task4(util.numList)       # pass variable numList from utilities.py

  input('Press enter to quit.')  # pause at the end of the program

if __name__ == "__main__":
    main()