# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


'''Take a list of strings and an integer n as parameters
Use a for loop to iterate over the strings and count how many strings have n or more characters 
(you may use the len() function to calculate the number of characters in a string)
Return the count
Do NOT ask the user for any input. Do NOT print anything in your function.

some_string = 'How many vowels are there in this string?'
count = 0                        # initialize the count variable
for chr in some_string:          # loop over characters in the string
  if chr in 'aAeEiIoOuU':        # check if the character is a vowel
    count += 1                   # if True, increment count
print(f'There are {count} vowels in the string')
'''
def count_strings(lis, n):
    x = 0
    for char in lis:
        if len(char) >= n:
            x += 1
    return x

    
count_strings(['', 'a', 'aa', 'aaa'], 0)   # should return 4
count_strings(['', 'a', 'aa', 'aaa'], 2)   # should return 2 
count_strings(['', 'a', 'aa', 'aaa'], 4)   # should return 0


