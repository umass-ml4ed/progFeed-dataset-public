# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst,n):
    count = 0
    for i in lst:
        if len(i) >= n:
            count+=1
    return count

some_list = ['', 'a', 'aa', 'aaa']

print(count_strings(some_list,2))

#I am having trouble figuring out what must be returned
#In the lab instructions, it says to return an integer. Of what?
#The integer is of the count of some string
#Must return a number of strings containing the n amount of characters

#####Answer######

#If there are 4 strings with a, and n = 1, then the returned value should be the integer 4
#If there are 4 strings, 3 of them with a, and n = 1, the returned value should be the integer 3

#The return must be the # of strings containing the amount n
#Don't hard code. Make sure this can work for all values, not just one specific list or some specific parameter. 