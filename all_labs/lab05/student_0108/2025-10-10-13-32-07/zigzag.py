# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(int_lst):
    if(len(int_lst)<=3):
        return True
    else:
        for cnt in range (1, len(int_lst)-1):
            if((int_lst[cnt-1]>int_lst[cnt] and int_lst[cnt+1]>int_lst[cnt]) or int_lst[cnt-1]<int_lst[cnt] and int_lst[cnt+1]<int_lst[cnt]):
                continue
            else:
                return False
        return True
    
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
