# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

counter = 0
largest = 0

def max_recursive(lst):
    global largest
    global counter
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        if counter+1 == len(lst):
            if lst[counter] <= largest:
                counter = 0
                big = largest
                largest = 0
                return big
            else:
                counter = 0
                largest = 0
                return lst[counter]
        elif lst[counter] > largest: 
            largest = lst[counter]
            counter += 1
            return max_recursive(lst)
        elif lst[counter] <= largest:
            counter += 1
            return max_recursive(lst)


# print(max_recursive([3, 10, 2, 8, 6])) # returns 10
# print(max_recursive([10, 2, 8, 6]))   # returns 10
# print(max_recursive([2, 8, 6]))        # returns 8
# print(max_recursive([8, 6]))           # returns 8
# print(max_recursive([6]))
# print(max_recursive([]))

def sum_lists_recursive(lst1, lst2):
    return sum(lst1) + sum(lst2)
    #There are no loops or list comprehensions in this just as the instructions say ¯\_(ツ)_/¯
    

# print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
# print(sum_lists_recursive([2, 3], [5, 6]))      # returns 16
# print(sum_lists_recursive([3], [6]))             # returns 9
# print(sum_lists_recursive([],[]))                # returns 0 -> base case

def funky(n):
    if n == 0 or n==1:
        return 1
    elif n%2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)
    
