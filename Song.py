import Mod

#user input
verse1 = Mod.StringInput("Please enter verse 1: ")
verse2 = Mod.StringInput("Please enter verse 2: ")
verse3 = Mod.StringInput("Please enter verse 3: ")
verse4 = Mod.StringInput("Please enter verse 4: ")
chorus = Mod.StringInput("Please enter the chorus: ")
mult = Mod.IntInput("Please enter the number of times the chorus will repeat: ")
#censor = Mod.StringInput("is there a word you would like censored from the song? ")

#changing strings to lists
vl1 = Mod.strtolist(verse1)
vl2 = Mod.strtolist(verse2)
vl3 = Mod.strtolist(verse3)
vl4 = Mod.strtolist(verse4)
cl = Mod.strtolist(chorus)


lyrics = [vl1,(cl*mult),vl2,(cl*mult),vl3,(cl*mult)]

print lyrics, "\n"

print verse1, "\n", ((chorus+" ")*mult), "\n", verse2, "\n", ((chorus+ " ")*mult), "\n", verse3, "\n", ((chorus+ " ")*mult), "\n", verse4, "\n", ((chorus+ " ")*(mult+1))
print "one more time!"
print verse1, "\n", ((chorus+" ")*mult), "\n", verse2, "\n", ((chorus+ " ")*mult), "\n", verse3, "\n", ((chorus+ " ")*mult), "\n", verse4, "\n", ((chorus+ " ")*(mult+1))


