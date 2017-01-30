#Module functions for other programs 

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
    
#string to list

def strtolist(t):
    list = t.split()
    return list

#censor list
def parselist(lst, strg):
    for word in lst:
        if lst[word] == strg:
            lst[word] = "_________"
    return lst

    