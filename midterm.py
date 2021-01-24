#Midterm Exam
#Class:- EECS 1015
#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
#Student Id:- 217828

import random

#TASK0 Print Details
def task0():
    print("Midterm Exam - EECS1015\nName: Hoshner Tavadia\nStudent ID: 217828567\nEmail: hoshnertavadia@gmail.com / htavadia@my.yorku.ca\n\n")

#TASK1 Monthly Wage Calculator
def task1():
    print("\nKindly Enter The Following Details:")
    fname = input("Enter First Name :- ")
    fname = fname.title().strip()
    lname = input("Enter Last Name :- ")
    lname = lname.upper().strip()
    hrs = input("Number Of Hours You Work Per Week (Numbers Only):- ")
    hrs = float(hrs)
    hrwages = input("Enter Hourly Wages (Numbers Only):- ")
    hrwages = float(hrwages)
    wages = 4*hrs*hrwages
    tax = wages*0.25
    netwage = wages*0.75
    print(f"""Employee = {lname}, {fname}
 ${wages:.2f} \tMonthly Salary (gross)
-${tax:.2f} \t25% Tax Deduction
=${netwage:.2f} \tMonthly Salary (net)""")
    print("\n")

#TASK2 Restaurant Menu
def task2():
    print("\nRestaurant Menu")
    money = 10.00
    def print2(x):
        print(f"You Have ${x:.2f} - what item do you want?")
        print("1: Falafel\t$3.00")
        print("2: Pizza\t$6.00")
        print("3: Salad\t$1.50")
        print("4: Coffee\t$1.00")
        print("Enter 0 to exit")
    while money > 0:
        print2(money)
        order = int(input("Your Order :-  "))
        if(order==0):
            break
        elif (order==1):
            if(money>=3):
                print("Order For *falafel* confirmed.\n")
                money = money-3.00
            else:
                print("Sorry, you don't have enough money for that item.\n")
        elif (order == 2):
            if (money >= 6):
                print("Order For *pizza* confirmed.\n")
                money = money - 6.00
            else:
                print("Sorry, you don't have enough money for that item.\n")
        elif (order==3):
            if(money>=1.5):
                print("Order For *salad* confirmed.\n")
                money = money-1.50
            else:
                print("Sorry, you don't have enough money for that item.\n")
        elif (order==4):
            if(money>=1):
                print("Order For *coffee* confirmed.\n")
                money = money-1.00
            else:
                print("Sorry, you don't have enough money for that item.\n")
        else:
            print("Invalid menu item. Try Again.\n")
    print("Thank You!!")
    print("\n")

#TASK3 Dice Roll
def task3():
    print("\nDICE ROLL GAME\n")
    def game():
        six = 0
        print("\nGenerating Dice Roll.........")
        for x in range(0,10):
            y = random.randint(1,6)
            if y == 6:
                six = six+1
                print("*["+str(y)+"]*")
            else:
                print("["+str(y)+"]")
        if(six>1):
            print("You Win!!")
        else:
            print("You Lose :(")
        print()
        print("Play Again?? (Y/N)")
        play = input().upper().strip()
        if play =="Y":
           game()
        else:
           print('Thank You For Playing\n')
    game()


#TASK4 DNA SEQUENCE
def task4():
    def generateDNASequence():
        str = ""
        for x in range(40):
            y = random.randint(1,4)
            if (y==1):
                str = str+"A"
            elif (y==2):
                str = str+"C"
            elif (y==3):
                str =str+"G"
            else:
                str=str+"T"
        return str

    def applyGammaRadiation(str):
        mutate = random.randint(1,100)
        if mutate>50:
            ch = 1
            str1 = ""
            mutatedcharacter = random.randint(0,39)
            while ch==1:
                y = random.randint(1,4)
                if (y == 1):
                    ch ="A"
                elif (y == 2):
                    ch ="C"
                elif (y == 3):
                    ch ="G"
                elif (y==4):
                    ch ="T"
                if (str[mutatedcharacter]==ch):
                    ch=1

            str1=str[0:mutatedcharacter]+ch+str[mutatedcharacter+1:]
            return str1
        else:
            str1 = str
            return str1
            
        
            

    def detectMutation(x,y): # error showing fix asap
        mut = " "*40
        mut = mut
        for a in range(40):
            if (x[a]==y[a]):
                pass
            else:
                mut=mut[0:a]+"^"+mut[a+1:]
        return mut

    def print_result(orig,mod,loc):
        print(orig + "\t(Original DNA)")
        print(mod + "\t(DNA After Radiation)")
        print(z)
        if(orig==mod):
            print("NO MUTATION DETECTED")
        else:
            print("MUTATION DETECTED")

    DNA=generateDNASequence()
    mutDNA=applyGammaRadiation(DNA)
    z=detectMutation(DNA,mutDNA)
    print_result(DNA,mutDNA,z)





def main():
    task0()
    print("\n--TASK 1 --")
    task1()
    print("\n--Task 2 --")
    task2()
    print("\n--Task 3 --")
    task3()
    print("\n--Task 4 --\n")
    task4()
    input()

if __name__=="__main__":
    main()
