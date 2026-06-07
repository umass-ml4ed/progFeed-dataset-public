# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst)==1:
        return lst[0]
    if len(lst)==0:
        return 0
    return max_recursive(lst[:-1]) if lst[-1]<lst[-2] else max_recursive(lst[:-2]+[lst[-1]])

print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6]))    # returns 10
print(max_recursive([2, 8, 6]))        # returns 8
print(max_recursive([8, 6]))          # returns 8
print(max_recursive([6]))             # returns 6 -> base case
print(max_recursive([]))              # returns 0 -> base case

def sum_lists_recursive(lst1,lst2):
    if len(lst1)==0:
        return 0
    return sum_lists_recursive(lst1[1:],lst2[1:])+lst1[0]+lst2[0]

print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
print(sum_lists_recursive([3], [6]))             # returns 9
print(sum_lists_recursive([],[]))                # returns 0 -> base case

def funky(n):
    if n==0 or n==1:
        return 1
    elif n%2==0:
        return 2*funky(n//2)
    else:
        return 1+2*funky(n+1)
    
print(funky(2)) #2
print(funky(10)) #74
print(funky(50)) #554
print(funky(-10)) #50
print(funky(-50)) #418

def permutations(lis):
    if len(lis)==1:
        return [lis]
    retlis=[]
    for i in range(len(lis)):
        front_item=lis[i]
        remaining=lis[0:i]+lis[i+1:]
        for x in permutations(remaining):
            retlis.append([front_item]+x)
    return retlis

print(permutations(['AA','BB','CC']))

