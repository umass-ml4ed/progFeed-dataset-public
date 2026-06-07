# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----
'''implement a function called combine_lists. This function has two parameters: 
a list object with integers, and another list object with integers. You are asked to do the following tasks:

Take the two lists a and b as parameters. 
Insert the first element of b at the beginning of a.
Insert the last element of b at the end of a.
Delete the middle element of a. You may assume that a had an odd number of elements before the deletion. 
Return the resultant list a after all the changes. 


write a function, called classify_by_length, which should:
Take one list of integers, a as the parameter.
Return a string representing the list class. The string must be one of empty, odd_length, or even_length, and it may NOT be anything else. 
You should return empty if the list is empty.
You should return odd_length if the list has an odd length.
You should return even_length if the list has an even length.
The starter code contains example code that you can uncomment to help test your function. Follow the instructions there. Below are some examples of running a correct implementation of this function:
'''

def combine_lists(a, b):
    a.insert(0, (b[0]))
    a.append(b[-1])
    lis_a = len(a) // 2
    a.remove(lis_a)
    return a 

def classify_by_length(a):
    if (len(a) % 2) == 0 and (len(a) % 2) != 0:
        return 'even_length'
    if (len(a)) > 0:
        return 'odd_length'
    else:
        return 'empty' 
    
# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following lines (remove the # characters on each line)
# to test combine_lists()
#print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
#print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))

# Uncomment the following lines (remove the # characters on each line)
# to test classify_by_length()
print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))
