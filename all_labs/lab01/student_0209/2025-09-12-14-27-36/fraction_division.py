# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

dividend=int(input("What is the dividend: "))
divisor=int(input("What is the divisor: "))
quotient=dividend//divisor
remainder=dividend%divisor

print(str(dividend) + "/" + str(divisor) + " equals:")
print("\t" + str(quotient) + " and " + str(remainder) + "/" + str(divisor))