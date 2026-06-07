# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
a=float(input('enter a'))
b=float(input('enter b'))
c=float(input('enter c'))
d = (b**2) - (4*a*c)
x_1= (-b-math.sqrt(d))/(2*a)
x_2= (-b+math.sqrt(d))/(2*a)
print(f'{a}*x^2+{b}*x+{c} has roots:')
print(x_1)
print(x_2)