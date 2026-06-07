# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst)==0:
        return 0
    
    def helper(i):
        if i==len(lst)-1:
            return lst[i]
        
        rest_max=helper(i+1)
        if lst[i]>rest_max:
            return lst[i]
        else:
            return rest_max
        
    return helper(0)
#print(max_recursive([3, 10, 2, 8, 6]))
#print(max_recursive([10, 2, 8, 6]))  
#print(max_recursive([2, 8, 6]))       
#print(max_recursive([8, 6]))        
#print(max_recursive([6]))
#print(max_recursive([]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1)==0:
        return 0
    
    return (lst1[0] + lst2[0]) + sum_lists_recursive(lst1[1:], lst2[1:])
#print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) 
#print(sum_lists_recursive([2, 3], [5, 6])) 
#print(sum_lists_recursive([3], [6]))           
#print(sum_lists_recursive([],[])) 

def funky(n):
     if n==0 or n==1:
        return 1
     if n%2==0:
        return 2*funky(n//2)
     else:
        return 1+2*funky(n+1)
#print(funky(2)) 
#print(funky(10)) 
#print(funky(50))
#print(funky(-10)) 
#print(funky(-50)) 


