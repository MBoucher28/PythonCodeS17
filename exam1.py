#exam 1

#reads speeds and returns list of ints

def readData(filename):
    file = open(filename)
    speeds = []
    for line in file:
        speeds.append(int(line))
    return speeds

#calculates average of list of numbers

def getAverage(l):
    total = sum(l)
    length = len(l)
    avg = float(total/length)
    return avg

    

#counts number of speeders in list greater than or equal to 69mph

def countSpeeder(l, maxSpeed):
    speeders = 0
    for n in l:
        if n > maxSpeed:
            speeders = speeders + 1
    speeders = speeders/2
    return speeders



#main that calls all methods

def main():
    file1 = "data-rush.txt"
    file2 = "data-not-rush.txt"
    speedlimit = 69
    rushfine = 150
    nonrushfine = 100
    
    rushdata = readData(file1)
    nonrushdata = readData(file2)
    
    rushaverage = getAverage(rushdata)
    nonrushaverage = getAverage(nonrushdata)
    
    rushspeeders = countSpeeder(rushdata, speedlimit)
    nonrushspeeders = countSpeeder(nonrushdata, speedlimit)
    
    rushpayments = rushspeeders*rushfine
    nonrushpayments = nonrushspeeders*nonrushfine
    
    
    print "the average rush hour speed was %.2f" %rushaverage
    print "the average non rush hour speed was %.2f" %nonrushaverage
    print "the number of rush hour speeders is %i" %rushspeeders
    print "the number of non rush hour speeders is %i" %nonrushspeeders
    print "the fines paid during rush hour were: %i" %rushpayments
    print "the fines paid during non rush hour were: %i" %nonrushpayments
    
    




main()