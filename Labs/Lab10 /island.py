# -*- coding: utf-8 -*-
class Inhabitant:
    def __init__(self, name, affiliation):
        self.name = name
        self.affiliation = affiliation
        
    def are_you_a_liar(self):
        truth = self.affiliation == "liar"
        return self.what_i_would_say(truth)
    
    def are_they_a_liar(self, other):
        truth = other.affiliation == "liar"
        return self.what_i_would_say(truth)
    
    def are_you_both_liar(self, other):
        truth = (self.affiliation == "liar" and other.affiliation == "liar")
        return self.what_i_would_say(truth)
    
    def are_you_from_different_tribes(self, other):
        truth = (self.affiliation !=  other.affiliation)
        return self.what_i_would_say(truth)
        

class Truthteller(Inhabitant):
    def __init__(self, name):
        super().__init__(name, "truthteller")
        
    def what_would_i_say(self, truth):
        return truth
        
class Liar(Inhabitant):
    def __init__(self, name):
        super().__init__(name, "liar")
        
    def what_would_i_say(self, truth):
        return not truth
        
