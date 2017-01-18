#Meaghan Boucher
# 1/18/17
#program takes recipe given and changes the amounts based on the given conversion factor

#variable input
print "enter amount of flour in cups: ",
flour = raw_input()
print "enter amount of water in cups: ",
water = raw_input()
print "enter amount of salt in teaspoons: ",
salt = raw_input()
print "enter amount of yeast in teaspoons: ",
yeast = raw_input()
print "enter the adjustment factor: (i.e. 2 is double, 3 is triple)",
adj = raw_input()

#conversion math
newflour = (float(flour)*float(adj))
newwater = (float(water)*float(adj))
newsalt = (float(salt)*float(adj))
newyeast = (float(yeast)*float(adj))
#print cups recipe
print "here is your new recipe:"
print "flour (cups): %f" %newflour
print "water (cups): %f" %newwater
print "salt (tsp): %f" %newsalt
print "yeast (tsp): %f" %newyeast

#cups to grams conversion factors. this many grams in 1 unit of measure.
flourctg = 125
waterctg = 237
salttsptg = 5
yeasttsptg = 3

#conversion math
gramflour = newflour*flourctg
gramwater = newwater*waterctg
gramsalt = newsalt*salttsptg
gramyeast = newyeast*yeasttsptg

#print grams conversion
print "here is your recipe in grams:"
print "flour (grams): %f" %gramflour
print "water (grams): %f" %gramwater
print "salt (grams): %f" %gramsalt
print"yeast (grams): %f" %gramyeast