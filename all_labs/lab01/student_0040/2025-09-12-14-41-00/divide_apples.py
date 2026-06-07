# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED



import math

def apples():
    a = input("Enter total apples: ")
    b = input("Enter number of baskets: ")

    a = int(a)
    b = int(b)

    print(a,"apples for",b,"baskets can be divided as:\n",a // b,"apples per basket, and\n",a % b,"leftover apples.")

apples()

# 95 apples for 12 baskets can be divided as:
# 7 apples per basket, and
#  11 leftover apples.
    