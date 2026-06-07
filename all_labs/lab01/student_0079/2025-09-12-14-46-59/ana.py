# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# The task of this program is to read in two inputs from the user (using the input function):
# A string (let's call it "a")
# An integer (let's call it "n")

string = input("Enter a string: ")
integer = int(input("Enter an integer: "))
multistr = string * integer
print(multistr + str(integer) + multistr)