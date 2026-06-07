# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
n=int(input("integers:"))
a=input("strings:")
def pattern(n,a):
    output=a * n + str(n) + a * n
    return output
print(pattern(n,a))
