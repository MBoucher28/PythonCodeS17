#exam 6
suspects = ["MISS SCARLETT", "COL MUSTARD", "MR GREEN"]
weapons= ["PIPE", "CANDLESTICK", "WRENCH"]



def getList(suspects,weapons):
    possibilities = []
    for suspect in suspects:
        for weapon in weapons:
            possibilities.append(suspect.upper() + " " +weapon.upper()) 
    return possibilities

def clueType():
    clueType = raw_input("Is the clue a weapon or a suspect? (w/s)")
    if clueType == "s":
        clue = 0
    if clueType == "w":
        clue = 1
    return clue
    

def getClue(kind):
    if kind == 0:
        clue = raw_input("Enter the name of the suspect it can't be: ").upper()
    if kind == 1:
        clue = raw_input("Enter the weapon it can't be: ").upper()
    return clue
    
    
def main():
    poss = getList(suspects,weapons)
    while len(poss)>1:
        left = len(suspects) * len(weapons)
        print "you have " + str(left) + " possibilities left"
        kind = clueType()
        clue = getClue(kind)
        if kind == 0:
            if clue in suspects:
                suspects.remove(clue)
                poss = getList(suspects,weapons)
        if kind == 1:
            if clue in weapons:
                weapons.remove(clue)
                poss = getList(suspects,weapons)
        
    print "the final answer is " + poss[0]

main()


