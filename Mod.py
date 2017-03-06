#Module functions for other programs 
import random
#get int input from user

def IntInput(s):
    print s,
    num = int(raw_input())
    return num

#get string input from user

def StringInput(i):
    print i,
    inpt = raw_input()
    return inpt


def randomincreasing(n,x,y):
    n = n + random.randrange(x, y)
    return n

#string to list

def strtolist(t):
    list = t.split(", ")
    return list

def readfile():
    file = open("temps.txt")
    for line in file:
        words = line.split(", ")
    for i in words:
        words.append(float(i))
    return words
    
def calculateave(L,S,E):
    for num in L:
        top = 0
        top = float(top + L[num])
        bot = 0
        bot = float(bot + 1)
    avg = top/bot
    return avg
    

def count(L,S,E):
    for num in L:
        count = 0
        if L[num] > 0:
            count = count + 1
    return count
    

def userpercentinput(L):
    percent = IntInput("what position in the list would you like to start? ")
    return percent
    
def beginorend():
    begin = 7
    end = 7
    input = StringInput("would you like to go from the beginning or the end (b/e)")
    if input == "b" or "e":
        if input == "b":
            begin = 1
            return begin
        elif input == "e":
            end = 0
            return end
    else:
        print("sorry, that wasn't right")
    
    
def main():
    file = readfile()
    split = userpercentinput(file)
    start = beginorend()
    if start == 1:
        average1 = calculateave(file,0,split)
        count1 = count(file,0,(len(file)+1))
    if start == 0:
        average2 = calculateave(file,split,(len(file)+1))
        count2 = count(file,split,(len(file)+1))
    
    print "the average of the first %f years is %f" % split,average1
    print "the number of years it has been positive is %i" %count1
    print "the average of the last %f years is %f" %(len(file)-split),average2
    print "the number of years it has been positive is %i" %count2
    

    
    
    
    
    
    