def is_zigzag(a):
    if len(a)<3:
        return True
    for i in range(1,len(a)-1):
        if (int(a[i])>int(a[i-1]) and int(a[i])>int(a[i+1])):
            if not (int(a[i])<int(a[i-1]) and int(a[i])<int(a[i+1])):
                return True
            else:
                return False
        elif (int(a[i])<int(a[i-1]) and int(a[i])<int(a[i+1])):
            if not (int(a[i])>int(a[i-1]) and int(a[i])>int(a[i+1])):
                return True
            else:
                return False
        else:
            return False
        
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
