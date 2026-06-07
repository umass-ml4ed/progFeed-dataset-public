# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))


def is_edge_sorted(a, b, c):
    if a <= b and b <= c:
        return True 
    else: 
        return False 


print(is_edge_sorted(3, 4, 5))

print(is_edge_sorted(3, 5, 3))

