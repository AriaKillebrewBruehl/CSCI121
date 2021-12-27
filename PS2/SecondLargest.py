# -*- coding: utf-8 -*-

def two_largest() :
    print("This program finds the two largest integers.")
    print("Enter a blank line to stop.")
    
    
    
    largest = int(input("? "))
    seclargest = int(input("? "))
    
    if largest < seclargest:
        largest, seclargest = seclargest, largest 
        
    temp = input("? ")
     
    while temp != "":
        
        temp = int(temp)
       
        if temp > largest:
            largest, seclargest = temp, largest 
            
    
        if temp < largest and temp > seclargest:
            seclargest = temp 
        
        temp = input("? ")
        
        
    print("The largest value is " + str(largest) + ".") 
    print("The second-largest is " + str(seclargest) + ".")
    