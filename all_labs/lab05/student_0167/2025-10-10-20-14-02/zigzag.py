# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list_of_integers):
    if len(list_of_integers) < 3:
        return True
    else:
        for i in range(1,len(list_of_integers)-1):
            if ((list_of_integers[i] > list_of_integers[i+1]) and (list_of_integers[i] > list_of_integers[i-1])) or ((list_of_integers[i] < list_of_integers[i-1]) and (list_of_integers[i] < list_of_integers[i+1])):
                continue
            else:
                return False
        return True
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False

