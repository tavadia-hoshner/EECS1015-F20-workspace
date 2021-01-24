#Lab 4
#Class:- EECS 1015
#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
#Student Id:- 217828567

from random import randint

def drawcards():
    card1 = randint(2,14)
    card2 = randint(2,14)
    if(card1<card2):
        x = card1
        card1 = card2
        card2 = x
    return card1, card2

def card2str(card):
    str=""
    if(card<11):
        str=f"{card}"
    elif(card==11):
        str="J"
    elif (card == 12):
        str = "Q"
    elif (card == 13):
        str = "K"
    elif(card==14):
        str = "A"
    return str

def printhand(a,b,c):
    print(f"[{a}] [{b}] "+c)


def printoutcome(a,b,c,d):
    result = 0
    if(a==b):#checks if players cards are pairs
        ycardpair = True
    else:
        ycardpair = False
    if(c==d):#checks if computers cards are pairs
        ccardpair = True
    else:
        ccardpair = False

    if (ycardpair == True) and (ccardpair == True):
        if(a>c):
            result = 1
        elif(a<c):
            result = 2
    elif (ycardpair == True) and (ccardpair == False):
        result = 1
    elif (ycardpair == False) and (ccardpair == True):
        result = 2
    else:
        if (a > c):
            result = 1
        elif (a < c):
            result = 2
        elif (a==c):
            if(b>d):
                result = 1
            elif (b<d):
                result = 2
    if(result==1):
        print("       You Win!!!")
    elif(result==2):
        print("       You Lose :(")
    else:
        print("       Its A Tie")



def main():
    print("Welcome To Two Card Poker Game")
    input("****Press Any Key To Begin****\n")
    while(1>0):
        a,b = drawcards()
        c,d = drawcards()
        ycard1 = card2str(a)
        ycard2 = card2str(b)
        ccard1 = card2str(c)
        ccard2 = card2str(d)
        printhand(ycard1,ycard2,"Your Cards")
        printhand(ccard1,ccard2,"Computer's Cards")
        printoutcome(a,b,c,d)
        print("\nWould You Like To Play Again(Y/N)?")
        ch = input()
        ch = ch.upper()
        if(ch=="N"):
            print("\n****Thank You For Playing****")
            input()
            break
        elif(ch=="Y"):
            print("\n\n**TWO CARD POKER GAME**")
            continue
        else:
            print("Invalid Input, Play Game Again\n\n**TWO CARD POKER GAME**")

if __name__=="__main__":
    main()