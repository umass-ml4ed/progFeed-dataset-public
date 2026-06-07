# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def is_zigzag(my_list):
    n = len(my_list)
    if(n < 3):
        return True
    for i in range(1, n-1):
        if(my_list[i] > my_list[i - 1] and my_list[i] >  my_list[i + 1]):
            continue
        elif(my_list[i-1] > my_list[i] and my_list[i + 1] > my_list[i]):
            continue
        else:
           return False
    return True
print(is_zigzag([1, 3, 2, 4, 5]))