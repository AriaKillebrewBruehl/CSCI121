# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, name, species, age, age_multiplier, sound):
        self.name = name
        self.species = species
        self.age = age
        self.age_multiplier = age_multiplier
        self.sound = sound
    
    def getAge(self):
        return self.age
    
    def getHumanAge(self):
        return self.age_multiplier * self.age
    
    def poke(self):
        return self.sound
        
        
        
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, "dog", age, 7, "woof")
        
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "cat", age, 6, "meow")
        
class Tiger(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.speacies = "tiger"
        self.poke = "rawr"
        
class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, "elephant", age, 1, "*trumpet noise*")
        
class Bear(Animal):
    def __init__(self, age):
        super().__init__("Yogi", "bear", age, 2, "rawr")
        
class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, "bird", age, 10)
        
class Zebra(Animal):
    def __init__(self, name, age):
        super().__init__(name, "zebra", age, 3)
        
class Goat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "goat", age, 4)

class Lama(Animal):
    def __init__(self, name, age):
        super().__init__(name, "lama", age)
        
class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, "fish", age)
 
