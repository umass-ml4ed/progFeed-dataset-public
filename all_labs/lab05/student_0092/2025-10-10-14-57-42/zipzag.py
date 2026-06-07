# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst:list) -> bool:
    # if len(lst) == 2:
    #     return True
    # for i in lst:
    #     if (i > lst[i-1] and i > lst[i+1]) or (i < lst[i-1] and i < lst[i+1]):
    #         return True
    # return False
    if len(lst) <= 2:
        return True
    checklist = []
    for i in lst:
        if lst.index(i) == 0:
            if i < lst[i+1] or i > lst[i+1]:
                checklist.append(True)
            else:
                checklist.append(False)
        elif lst.index(i)+1 == len(lst):
            if i < lst[i-1] or i > lst[i-1]:
                checklist.append(True)
            else:
                checklist.append(False)
        else:
            if (i > lst[lst.index(i)-1] and i > lst[lst.index(i)+1]) or (i < lst[lst.index(i)-1] and i < lst[lst.index(i)+1]):
                checklist.insert(-2, True)
            else:
                checklist.insert(-2, False)
    return False not in checklist

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False