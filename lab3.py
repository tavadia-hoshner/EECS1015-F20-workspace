#Lab 3
#Class:- EECS 1015
#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
#Student Id:- 217828567

#TASK 1
print("---TASK 1: Determine Fare---")
age = int(input("Enter Your Age :-  "))
sdt = input("Are You A Student (Y/N)? :-")
typ = ""
price = "$"
if (age<=12):
    typ = "CHILD"
    price =price+"0.50"
elif ((sdt.strip().upper())=="Y"):
    typ = "STUDENT"
    price = price+"1.00"
elif (age>=65):
    typ = "SENIOR"
    price = price + "0.50"
else:
    typ = "ADULT"
    price = price + "1.50"
print(f"Ticket type = {typ}\nTicket Price = {price}")
print("------TASK 1 COMPLETE------\n")


#TASK 2
print("---Task 2: Print stringing Characters and Reverse --")
string = input("Input a string :- ")
leng = len(string)
sent = ""
for x in range (0,leng):
    char = string[x:x+1]
    print(f"str[{x}] = '{char}'")
    sent = char+sent
print("Reversed :- '"+sent+"'")
print("------TASK 2 COMPLETE------\n")


#TASK 3
print("---Task 3: The Maximum ----\nKeep entering positive numbers.\nTo quit, input enter a negative number")
max = 0
n = int(input("Enter A Number :- "))
while(n>=0):
    if(n>max):
        max = n
    n = int(input("Enter A Number :- "))
print("Largest Number Entered = "+ str(max))
print("------TASK 3 COMPLETE------\n")


#TASK 4
print("---Task 4: String triangle ---")
str = input("Type In A String :- ")
str = str.strip()
leng = len(str)
for x in range(1,leng+1):
    print(str[0:x])
for x in range(1,leng):
    print(str[0:leng-x])
print("------TASK 4 COMPLETE------\n")
input()

