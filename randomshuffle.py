import Mod
import random

rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suit = ['Clubs','Hearts','Diamonds','Spades']


#create deck in number/suit order
def buildDeck(rank,suit):
    deck = []
    for n in range(13):
        for i in range(4):
            card = rank[n] + " of " + suit[i]
            deck.append(card)
    return deck
            

#shuffle deck randomly
def shuffleDeck(deck):
    random.shuffle(deck)
    return deck
    
#deal top 5 cards of the deck
def dealDeck(deck):
    top5 = deck[:5]
    return top5
    
    
    
def main():
    shuffleamount = Mod.IntInput("How many times would you like to shuffle the deck? ")
    n = 0
    deck = buildDeck(rank,suit)
    while n < shuffleamount:
        deck = shuffleDeck(deck)
        hand = dealDeck(deck)
        n = n + 1
        
    print "this is your hand:"
    print hand
    
    
    
main()