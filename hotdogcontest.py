#assignment 5: hot dog contest
import Mod
import random
import time

def main():
    #variables
   
    cash = 1
    
    #money while loop
    while cash > 0:
        userbet = 0
        cash = 100
        userguess = Mod.StringInput("enter the contestant you think will win: (sally, george, mark)")
        print "you start with %i" %cash
        userbet = Mod.IntInput("enter your bet:") %cash
        hotdog1 = 0
        hotdog2 = 0
        hotdog3 = 0
        while hotdog1<50 and hotdog2<50 and hotdog3 < 50:
            hotdog1 = hotdog1 + random.randrange(0, 4)
            hotdog2 = hotdog2 + random.randrange(0, 4)
            hotdog3 = hotdog3 + random.randrange(0, 4)
            print "sally has eaten %i hotdogs" %hotdog1
            print "george has eaten %i hotdogs" %hotdog2
            print "mark has eaten %i hotdogs" %hotdog3
            time.sleep(1)
            print "Chomp...Chomp...Chomp"
            time.sleep(1)
        print max(hotdog1,hotdog2,hotdog3)
        if max(hotdog1,hotdog2,hotdog3) == hotdog1:
            winner = "sally"
        if max(hotdog1,hotdog2,hotdog3) == hotdog2:
            winner = "george"
        if max(hotdog1,hotdog2,hotdog3) == hotdog3:
            winner = "mark"
        print winner
        if userguess is winner:
            print "congratulations! you win!"
            cash = cash + (cash*.5)
        else:
            print "sorry, you lose!"
            cash = cash - (cash*.5)
            
            


main()