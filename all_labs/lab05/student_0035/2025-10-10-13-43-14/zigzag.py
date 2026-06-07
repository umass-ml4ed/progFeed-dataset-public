# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def is_zigzag(my_list):
    n = len(my_list)
    if(n < 3):
        return True
    for i in range(1, n-1):
        if(my_list[i] > my_list[i - 1] and my_list[i] <  my_list[i + 1]):
            return False
            break
        elif(my_list[i-1] > my_list[i] and my_list[i + 1]  < my_list[i]):
            return False
            break
        else:
            continue
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
