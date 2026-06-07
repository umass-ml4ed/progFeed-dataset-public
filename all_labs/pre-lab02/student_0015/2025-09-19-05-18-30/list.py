# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

# Take input for strings a, b, c, d
a = input("Enter string a: ")
b = input("Enter string b: ")
c = input("Enter string c: ")
d = input("Enter string d: ")

# Create an empty list
lst = []

# Add a at the end of lst
lst.append(a)
print(lst)

# Add b at the end of lst
lst.append(b)
print(lst)

# Add c at the beginning of lst
lst.insert(0, c)
print(lst)

# Remove d from lst (assumes d is already in lst)
lst.remove(d)  # remove() finds the first occurrence and deletes it
print(lst)

# Print the length of lst
print("Length of list:", len(lst))
