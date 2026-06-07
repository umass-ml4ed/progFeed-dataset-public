# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import math

def apples():
    a = input("Enter total apples: ")
    b = input("Enter total baskets: ")

    a = int(a)
    b = int(b)

    c = a // b
    d = a % b

    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    
    print(a + " apples for\n" + b + " baskets can be divided as\n" + c + " apples per basket, and\n" + d + " leftover apples")

apples()