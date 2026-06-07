# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

user_string = input("Enter a string: ")
user_integer = int(input("Enter an integer: "))

def pattern(user_string, user_integer):
    return (user_string * (user_integer)) + str(user_integer) + (user_string * (user_integer))

print (pattern(user_string, user_integer))