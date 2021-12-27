# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, nm, sp, ag): #self is constructor
        self.name = nm
        self.species = sp
        self.age = ag
        
class petOwner:
    def __init__(self, nm, pts):
        self.name = nm
        self.pets = pts
    
mowgliTheCat = Animal("mowgli", "cat", 2)
tobyTheDog = Animal("toby", "dog", 14)
rosieTheDog = Animal("rosie", "dog", 13)
tootieTheTurtle = Animal("tootie", "turtle", 17)
ava = petOwner("ava", [tobyTheDog, mowgliTheCat, rosieTheDog, tootieTheTurtle])

def averageAge(animals):
    total = 0 
    for animal in animals:
        total += animal.age
    return total/len(animals)

def namesOfSpecies(animals, sp):
    names = []
    for animal in animals:
        if animal.species == sp:
            names.append(animal.name)
    namesofspecies =  " and ".join(names)
    return namesofspecies 

def dogsOwnedBy(name):
    return namesOfSpecies(name.pets, "dog")