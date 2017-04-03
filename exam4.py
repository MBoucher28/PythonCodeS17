#exam 4

def check(file,word):
    for line in file:
        if word.upper() in line.upper():
            print line
def getWord():
    word = raw_input("Please enter the word you'd like to search for: ")
    return word
    

def main():
    file1 = file('bread.txt')
    file2 = file('firstAid.txt')
    file3 = file('recipes.txt')
    file4 = file('trivia.txt')
    
    search = getWord()
    
    print "bread.txt: "
    check(file1,search)
    print "firstAid.txt: "
    check(file2,search)
    print "recipes.txt:"
    check(file3,search)
    print "trivia.txt"
    check(file4,search)
    
    
    
main()    