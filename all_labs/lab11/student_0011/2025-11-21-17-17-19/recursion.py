#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def max_recursive(lst):
    if len(lst)==1:
        return lst.pop()
    if lst[-1]<lst[-2] and len(lst)>1:
        lst.remove(lst[-1])
        return max_recursive(lst)
    elif lst[-1]>lst[-2] and len(lst)>1:
        lst.remove(lst[-2])
        return max_recursive(lst)
    
    
print(max_recursive([1,2,3,4, 8, 100, 90]))