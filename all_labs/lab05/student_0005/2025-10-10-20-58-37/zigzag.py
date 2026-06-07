# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zig_zag(lst):
    for i in lst:
        if ((lst[i] < lst[i-1]) and (lst[i] < lst[i+1])) or ((lst[i] > lst[i-1]) and (lst[i] > lst[i+1])):
            return True
        else:
            return False
        
print(is_zig_zag([1, 3, 2, 4, 3]))
print(is_zig_zag([1, 4, 2, 5, 3]))
print(is_zig_zag([1, 2, 3, 4]))
# print(is_zig_zag([10]))
print(is_zig_zag([1, 3, 2, 4, 5]))