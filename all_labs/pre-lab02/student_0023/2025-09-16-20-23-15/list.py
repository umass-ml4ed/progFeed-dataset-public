# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# Read in four strings from the user
a = input("Enter a string for 'a': ")
b = input("Enter a string for 'b': ")
c = input("Enter a string for 'c': ")
d = input("Enter a string for 'd': ")

# Create an empty list
lst = []

# Add 'a' at the end and print
lst.append(a)
print(lst)

# Add 'b' at the end and print
lst.append(b)
print(lst)

# Add 'c' at the beginning and print
lst.insert(0, c)
print(lst)

# Remove 'd' from the list and print
# This assumes 'd' is in the list, as per the instructions.
lst.remove(d)
print(lst)

# Print the length of the list
print(len(lst))
