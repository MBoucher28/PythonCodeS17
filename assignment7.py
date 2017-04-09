import json


def getAnimals():
    file = open("animals.json")
    jlist = ""
    for line in file:
        line = line.strip()
        jlist = jlist + line
    animals = json.loads(jlist)
    return animals

def getStats(animals):
    name = raw_input("enter the name of an animal you would like to view: ")
    for animal in animals:
        if animal["Name"] == name:
            print "%s" %animal["Breed"]
            print "%s" %animal["age"]

def getBreed(animals):
    breed = raw_input("enter a breed: (Dog or Cat)")
    for animal in animals:
        if animal["Breed"] == breed:
            print "%s" %animal["Name"]



def main():
    
    animals = getAnimals()
    getStats(animals)
    getBreed(animals)
    
    

main()