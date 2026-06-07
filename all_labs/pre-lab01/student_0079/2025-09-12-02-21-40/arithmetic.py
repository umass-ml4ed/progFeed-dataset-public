# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# The task of this program is to read in two inputs from the user, store each in a separate variable:
# 1. A positive integer (let’s call it “a”)
# 2. Another positive integer (let’s call it “b”)

aS = input("Enter a: ")
bS = input("Enter b: ")
a = int(aS)
b = int(bS)

print("Addition: " + str(a + b))
print("Multiplication: " + str(a * b))
print("Division: " + str(a / b))
print("Integer Division: " + str(a // b))
print("Remainder: " + str(a % b))