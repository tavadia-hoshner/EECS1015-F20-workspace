#Lab 8
#Class:- EECS 1015
#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
#Student Id:- 217828567

from random import randint

class Bacteria:
    chance=0
    maxlife=0
    
    def __init__(self,ch,ml):
        Bacteria.chance = ch
        Bacteria.maxlife = ml
        self.life = randint(1,Bacteria.maxlife)
        self.day = 0

    def live_a_day(self):
        rand = randint(1,100) #if statement needed
        self.day=self.day+1
        if rand<Bacteria.chance:
            x=Bacteria(Bacteria.chance,Bacteria.maxlife)
            return x
        else:
            return None
    def is_alive(self):
        if self.life>self.day:
            return True
        else:
            return False


class Colony:


    def __init__(self,sb):
        self.stbact=sb
        Colony.totalmembers=sb
        Colony.days_gone = 0
        Colony.clist = []
        Colony.bers = 0
        Colony.total_dead = 0
        for i in range(0,self.stbact):
            x = Bacteria(Colony.chance,Colony.maxlife)
            Colony.clist.append(x)



    def live_a_day(self,printDailyReport=True):
        Colony.days_gone=Colony.days_gone+1
        self.newb = 0
        self.deadb = 0
        for x in range(len(Colony.clist)):
            if x<len(Colony.clist):
                y=Colony.clist[x].live_a_day()
                if y != None:
                    Colony.clist.append(y)
                    self.newb=self.newb+1
                    Colony.totalmembers=Colony.totalmembers+1
                z =Colony.clist[x].is_alive()
                if z==False:
                    del Colony.clist[x]
                    self.deadb = self.deadb + 1
                    Colony.total_dead=Colony.total_dead+1
        if printDailyReport:
            print("Day  %5d  Colony Size:- %6d New Members:- %6d Expired Members:- %6d"%(Colony.days_gone,len(Colony.clist),self.newb,self.deadb))

    def print_colony_status(self):
        size =Colony.get_colony_size(Colony)
        print(f"Colony Report At DAY {Colony.days_gone} \nCurrent Colony Population:\t{size}\nTotal number of bacteria:\t{Colony.totalmembers}\nTotal deceased bacteria:\t{Colony.total_dead}\n")

    def get_colony_size(self):
        return len(Colony.clist)




def main():
    count=0
    run =1
    cond = True
    while cond:
        print("Run",run)
        days = int(input("Max number of days to let colony grow: "))
        stbact = int(input("Number of starting bacteria: "))
        Colony.chance = int(input("% chance of daily division [1-100]: "))
        Colony.maxlife = int(input("Maximum lifespan for a bacteria (1 or greater): "))
        print("\n")
        x=Colony(stbact)
        for d in range(days):
            if (len(Colony.clist)>0and len(Colony.clist)<=50000):
                x.live_a_day()
        print("---Experiment Stopped/Ended---")
        x.print_colony_status()
        colsize= max(Colony.get_colony_size(x),Colony.totalmembers)
        count = count + colsize
        print("Total Number Of Bacteria Created = ",count)
        repeat = input("Would You Like To Run The Experiment Again? (Y/N)").upper()
        if repeat == 'Y':
            cond = True
            run = run+1
            print("\n\n")
        else:
            cond = False
            print("----End Of Experiment----")
            input()






main()






