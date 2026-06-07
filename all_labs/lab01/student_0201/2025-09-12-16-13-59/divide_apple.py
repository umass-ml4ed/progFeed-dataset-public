# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

a = input('Enter total apples: ')
b = input('Enter number of baskets: ')
a = int(a)
b = int(b)

def divide(a,b):
    result1 = a/b
    result2 = a%b
    return result1
    return result2
res1 = int(divide(a, b))
res2 = (a%b)

print(str(a) + ' apples for')
print(str(b) + ' baskets can be divided as:')
print(str(res1) + ' apples per basket, and')
print(str(res2) + ' leftover apples.')