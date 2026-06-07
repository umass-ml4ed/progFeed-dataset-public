# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED



import math

def apples():
    a = input("Enter total apples: ")
    b = input("Enter number of baskets: ")

    a = int(a)
    b = int(b)

    d = a // b
    r = a % b

    a = str(a)
    b = str(b)
    d = str(d)
    r = str(r)

    print(a + " apples for\n" + b + " baskets can be divided as\n" + d + " apples per basket, and\n" + r + " leftover apples.")

   # print(a,"apples for\n",b,"baskets can be divided as:\n",a // b,"apples per basket, and\n",a % b,"leftover apples.")

apples()

# 95 apples for 
# 12 baskets can be divided as:
# 7 apples per basket, and
#  11 leftover apples.
    