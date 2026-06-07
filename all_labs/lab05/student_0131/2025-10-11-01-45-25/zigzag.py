# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(lst):
    # If the list is too short, it is automatically zigzag
    if len(lst) < 3:
        return True

    for i in range(1, len(lst) - 1): 
        left = lst[i - 1]
        middle = lst[i]
        right = lst[i + 1]

        if middle > left and middle > right:
            continue  
        elif middle < left and middle < right:
            continue  
        else:
            
            return False

    
    return True
    