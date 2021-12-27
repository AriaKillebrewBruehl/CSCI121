# -*- coding: utf-8 -*-

def hailstone(n):
    count = 0
    num = int(n)
    
    while True:
        
        if num==1: break
             
        
        elif num%2 == 0:
            num = num//2
            
            print(str(num*2) + " is even, so I take half: " + str(num))
            count += 1
            
        else: 
            num = 3*num + 1 
            
            print(str((num-1)//3) + " is odd, so I make 3n+1: " + str(num))
            count += 1 
            
         
        
    print("The process took " + str(count) + " steps to reach 1.")
            