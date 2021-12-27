# File: FindPerfect.py

"""
This program lists all perfect numbers between the specified limits.
"""

# Constants


def isPerfect(n):
    """
    Returns True if the number n is a perfect number, which is an integer
    that is equal to the sum of its proper divisors.
    """
    return n == sumOfProperDivisors(n)

def sumOfProperDivisors(n):
    """
    Returns the sum of the proper divisors of n.
    """
    sum = 0
    for i in range(1, n):
        if isDivisibleBy(n, i):
            sum += i
    return sum

def isDivisibleBy(x, y):
    """
    Returns True if x is divisible by y.
    """
    return x % y == 0

# Test program


            
def convertBinary(i):
    binary = ""
    
    while i > 0:
        r = str(i%2)
        binary = r + binary
        i = i//2
    print(binary)  
# Startup code
def perfectBinaryNumbers(UPPER_LIMIT):
     for i in range(1, UPPER_LIMIT):
        if isPerfect(i):
            
            convertBinary(i)

