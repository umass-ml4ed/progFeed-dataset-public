# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

"""The first line should have numbers from n down to 1. Then have a newline ('\n'). 
The newline is a special character that can be used to print a new line when used inside a string.
For example, try printing the string 'abc\ndef'
The second line should start from n-1 down to 1. Then have a newline ('\n')
Continue until the last line has just 1. Then have a newline ('\n')
Each line’s numbers should be separated by a single space."""

def pyramid(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()  


"""We often need to combine two dictionaries that have overlapping keys.
Write a function, called merge_dicts, which should:
Take two dictionaries, d1 and d2, as parameters.
Return a new dictionary that contains all keys from both d1 and d2.
If a key appears in both dictionaries, its value in the result should be the sum of the two values"""

def merge_dicts(d1, d2):
    result = d1.copy()
    for key in d2:
        if key in result:
            result[key] = result[key] + d2[key]
        else:
            result[key] = d2[key]
    return result