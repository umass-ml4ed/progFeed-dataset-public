# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def classify_by_length(a):
    len_lst = len(a)
    if(len_lst == 0):
        return "empty"
    elif(len_lst & 1):
        return "odd_length"
    elif(len_lst & 0):
        return "even_length"

print(classify_by_length(a))