# -*- coding: utf-8 -*-

def digital_root(n):
    
    sum = n 
    
    while sum >= 10:
        
        
        n = sum 
        sum = 0
        
        while n != 0:
        
            sum += n%10
            n = n//10 
       
    return sum 
            
                
                
    
    
    
    
        
        