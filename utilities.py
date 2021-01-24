#####################
# EECS1015 - York University
# Final Exam - utilities.py
#
# IMPORTANT - Please put your info below
# Name: Hoshner Tavadia
# Student ID: 217828567
# email address: hoshnertavadia@gmail.com / htavadia@my.yorku.ca
#
#####################

from random import randint

# variable for task 1
lyrics = """It might seem crazy what I'm 'bout to say
Sunshine she's here, you can take a break
I'm a hot air balloon that could go to space
With the air, like I don't care baby by the way
Huh, because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do."""

# variable for task2
nameDict = {"Kai":19, "Bailey":19, "Su":21, "Mahesh":18, "Abdullah":18,
            "Dirk":17, "Franck":18, "Ollie":19, "Parsa":19, "Svetlana":24, "Jol":20, "Abbo":21,
            "Xavier":18, "Sarah":17, "Ming":19, "Seonjoo":20, "Pravel":22, "Urzula":22, "Javier":19,
            "Beatrice":20, "Olivia":21, "Bosko":17, "Katja":23, "Maxim":18, "Cameron":17, "Priya":18}

# variable for task3
raster = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

# variable for task 4
numList = [21, 20, 29, 16, 16, 19, 26, 19, 26, 23, 19, 25, 16, 18, 18, 18, 21, 15, 18,
           14, 22, 17, 32, 30, 22, 28, 26, 17, 19, 16, 17, 17, 19, 21, 20, 17, 18, 34, 23,
           18, 23, 22, 17, 22, 16, 11, 21, 26, 20, 27]

class listStats:

    def __init__(self, lista, clevel):
        self.olist = lista.copy()
        self.chance = clevel
        for x in self.olist:
            self.ch = randint(1,100)
            if self.ch<=self.chance:
                self.no = randint(1,100)
                pos = self.olist.index(x)
                if self.no<50:
                    self.olist[pos] = -1
                else:
                    self.olist[pos] = 100


    def computeMean(self):
        self.leng = len(self.olist)
        self.sum = 0
        for x in self.olist:
            self.sum = self.sum + x
        self.mean = self.sum/self.leng
        print("Standard Mean\t %.2f"%self.mean)

    def computeTrimmedMean(self):
        self.list1 = self.olist.copy()
        self.list1.sort()
        self.list1 = self.list1[10:-10]
        self.leng = len(self.list1)
        self.sum = 0
        for x in self.list1:
            self.sum = self.sum + x
        self.tmean = self.sum/self.leng
        print("Trimmed Mean\t %.2f" % self.tmean)

    def computeMedian(self):
        self.olist.sort()
        self.length = len(self.olist) #50
        mid = (self.length//2)
        self.median = self.olist[int(mid)-1]
        print("Median\t\t %2d" % self.median)

    def printStatistics(self):
        print("Corrupton Level",self.chance,"%")
        print(self.olist)
        self.computeMean()
        self.computeTrimmedMean()
        self.computeMedian()
        print("\n")


