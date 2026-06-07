def is_zigzag(a):
    if len(a)<3:
        return True
    b=len(a)
    c=a[1:-1:2]
    for i in c:
        g=a.index(i)
        if not (i>a[g-1] and i>a[g+1] or i<a[g-1] and i<a[g+1]):
            return False
    return True
 

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
