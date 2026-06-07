# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

userString = input("Enter a string: ")

while True:
    try:
        userInt = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Please enter a valid integer")

print(userInt*userString + str(userInt) + userInt*userString)