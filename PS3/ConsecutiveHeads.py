# -*- coding: utf-8 -*-
import random 

def consecutiveHeads(n):
    list = ["Heads", "Tails"]
    c = 0 
    t = 0
    
    def consecutiveHeadsHelp(n, c, t):
        flip = random.choice(list)
        
        if flip == "Heads":
            c += 1
            t += 1
            print("Heads")
           
        elif flip == "Tails":
            c = 0 
            t += 1 
            print("Tails")
            
        if c == 3:
           print("It took " + str(t) + " tosses to get " + str(n) + " consecutive heads." ) 
            
        else:
            consecutiveHeadsHelp(n, c, t)
    consecutiveHeadsHelp(n, c, t)       
if __name__ == "__main__":
    consecutiveHeads(3)
           

   