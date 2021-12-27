# -*- coding: utf-8 -*-

def neighborhood():
    aria = 1

    def family1():
        aurora = 10
        austin = 5
        lura = 30
        allan = 50
        print(aria)
        
    def family2():
        susan = 50
        richard = 30
        sophia = 5
        chloe = 10 
        aria = 100
        print(aria)
        
        
    def family3():
        nonlocal aria
        larry = 1
        daisy = 10000000000
        aria = aria + 1
        print(aria)
            
            
    family1()
    family2()
    
def tester():
    print(12//5)