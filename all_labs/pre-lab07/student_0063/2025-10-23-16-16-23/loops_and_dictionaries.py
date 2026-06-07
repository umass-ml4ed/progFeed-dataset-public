# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

'''Write a function called pyramid(n) that generates the following pattern:
Given a positive integer n, print n lines.
The first line should have numbers from n down to 1. Then have a newline ('\n'). 
The newline is a special character that can be used to print a new line when used inside a string.
 For example, try printing the string 'abc\ndef'
The second line should start from n-1 down to 1. Then have a newline ('\n')
Continue until the last line has just 1. Then have a newline ('\n')
Each line’s numbers should be separated by a single space.'''

def pyramid(n):
    result = ""
    for num in range(n, 0, -1):
        line = ""
        for i in range(num, 0, -1):
            line += str(i)
            if i > 1:
                line += " " 
        result += line + "\n" 
    return result


print(pyramid(4))

'''We often need to combine two dictionaries that have overlapping keys. 
Write a function, called merge_dicts, which should:
Take two dictionaries, d1 and d2, as parameters.
Return a new dictionary that contains all keys from both d1 and d2.
If a key appears in both dictionaries, its value in the result should be the sum of the two values.
'''

def merge_dicts(d1, d2):
    merged = {}
    for x in d1:
        merged[x] = d1[x]
    for x in d2:
        if x in merged:
            merged[x] += d2[x]  # sum values
        else:
            merged[x] = d2[x]
    return merged
    


    
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# {'a': 1, 'b': 5, 'c': 4}

print(merge_dicts({'x': 10}, {'y': 20}))
# {'x': 10, 'y': 20}

print(merge_dicts({}, {'a': 5}))
# {'a': 5}

print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
# {'a': 1, 'b': 7, 'c': 3, 'd': 10}
