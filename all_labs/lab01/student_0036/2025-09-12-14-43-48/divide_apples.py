# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import math

def divide_apples():
    a=input("Enter total apples: ")
    b=input("Enter number of baskets: ")
    c=int(a)//int(b)
    d=int(a)%int(b)
    print(a,"apples for",b,"baskets can be divided as:",c,"apples per basket,","and",d,"leftover apples.")
divide_apples()