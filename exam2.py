#exam 2
doc = "times.txt"

def readFile(FileName):
    d = {}
    for line in open(FileName):
        temp = line.split(",")
        name = temp[0].strip()
        time = float(temp[1].strip())
    return d
    
    
list = readFile(doc)

print list
