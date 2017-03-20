#exam 3
import random

def ChooseDuplicate(l):
    random.shuffle(l)
    s = random.randrange(0,8)
    return l[s]
    
def AddDuplicate(s,l):
    l.append(s)
    random.shuffle(l)
    return l
    
def ChooseNumber():
    num = -1
    while num < 0 or num > 9:
        num = int(raw_input("Please enter a number 0-9:"))
    return num
    
def Compare(s,q):
    win = False
    if s == q:
        win = True
        print "You Win!"
    return win
    

def main():
    choices = ['bird', 'dog', 'fish', 'snake', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
    trys = 0
    ChoiceA = 'a'
    ChoiceB = 'b'
    duplicate = ChooseDuplicate(choices)
    CardSet = AddDuplicate(duplicate,choices)
    print CardSet
    while Compare(ChoiceA,ChoiceB) is False:
        print "first number: "
        A = ChooseNumber() 
        print "second number: "
        B = ChooseNumber()
        while A == B:
            print "your numbers cannot be the same, please pick new numbers"
            A = ChooseNumber()
            B = ChooseNumber()
        ChoiceA = CardSet[A]
        print "your first card is %s" %CardSet[A]
        ChoiceB = CardSet[B]
        print "your second card is %s" %CardSet[B]
        trys = trys + 1
    print "it took you this many tries: %i" %trys

main()