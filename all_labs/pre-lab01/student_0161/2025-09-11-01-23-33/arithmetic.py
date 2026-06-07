# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

num1 = int(input("Enter a: "))
num2 = int(input("Enter b: "))

addition = num1+num2
mult = num1*num2

if num2!=0:
    div=num1/num2
    int_div=num1//num2
    remainder=num1%num2
else: 
    div=0
    int_div=0
    remainder=0
    

print(addition)
print(mult)
print(div)
print(int_div)
print(remainder)

#print(f"Addition: {addition}\nMultiplication: {mult}\nDivision: {div}\nInteger Division: {int_div}\nRemainder: {remainder}\n")