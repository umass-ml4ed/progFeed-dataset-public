# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 0:
        return 0
    if lst[0] > lst[1]:
        lst.pop(1)
    else:
        lst.pop(0)
    return max_recursive(lst)
    

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        num1 = 0
    else:
        num1 = lst1.pop(0)
    if len(lst2) == 0:
        num2 = 0
    else:
        num2 = lst2.pop(0)
    
    if len(lst1) == 0 and len(lst2) == 0:
        return num1 + num2

    else:
        return num1 + num2 + sum_lists_recursive(lst1, lst2)
    
def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0:
        return 2 * int(funky(n//2))
        
    else:
        return 1+ (2 * int(funky(n+1)))
       

print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6]))   # returns 10
print(max_recursive([2, 8, 6]))       # returns 8
print(max_recursive([8, 6]))          # returns 8
print(max_recursive([6]))             # returns 6 -> base case
print(max_recursive([]))             # returns 0 -> base case

print("\n\n")

print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
print(sum_lists_recursive([3], [6]))            # returns 9
print(sum_lists_recursive([],[]))               # returns 0 -> base case

print("\n\n")

print(funky(2)) #2
print(funky(10)) #74
print(funky(50)) #554
print(funky(-10)) #50
print(funky(-50)) #418



