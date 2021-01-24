#Lab 2
#Class:- EECS 1015
#Author:- Hoshner Tavadia
#Email:- hoshnertavadia@gmail.com/htavadia@my.yorku.ca
#Student Id:- 217828567


#TASK1
print("-------")
print("TASK 1 :- Type in an exponent in the following form x^y, where x and y are single digits from 0-9")
exp = input("Type exponent here :  ")
number = int(exp[0])
power = int(exp[2])
result = number**power
print(f"{exp} is {result}")
print("\nTASK 1 Complete\n-------")

#TASK2
print("-------")
print("TASK 2 :- First Half Upper, Second Half Lower")
sent = input("Type a sentence :  ")
sent = sent.strip()
length = len(sent)
mid = length//2
mid_char = sent[mid]
upperchar = sent[0:mid].upper()
lowerchar = sent[mid:length].lower()
print(f"The String is {length} chars long. '{mid_char}' is the middle character.")
print("Modified Sentence: " + upperchar + "|" + lowerchar)
print("\nTASK 2 Complete\n-------")

#TASK3
print("-------")
print("TASK 3 :- Remove commas and periods. Convert spaces to * and characters to lowercase.")
sent2 = input("Type a sentence :  ")
sent2 = sent2.strip().replace(",","").replace(".","").replace(" ","*")
sent2 = sent2.lower()
print("Modified Sentence: "+sent2)
print("\nTASK 3 Complete\n-------")


#TASK4
print("-------")
print("TASK 4 :- Substring Highlight")
sent3 = input("Type a sentence :  ")
sent3 = sent3.strip()
substring = input("Type a Substring :  ")
modsub = substring.upper()
modsub = "*"+modsub+"*"
firstind = sent3.find(substring)
sublen = len(substring)
strlen = len(sent3)
lastind = firstind+sublen
result3 = sent3[0:(firstind)] + modsub + sent3[(lastind):strlen]
print("Modified Sentence : "+ result3)
print("\nTASK 4 Complete\n-------")
input()