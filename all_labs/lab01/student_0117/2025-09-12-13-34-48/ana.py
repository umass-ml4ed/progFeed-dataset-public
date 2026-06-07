# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

input = input("Enter your string followed by a space, then your integer: ")
input_as_list = input.split()
a = input_as_list[0]
n = input_as_list[1]
print(a*int(n) + str(n) + a*int(n))