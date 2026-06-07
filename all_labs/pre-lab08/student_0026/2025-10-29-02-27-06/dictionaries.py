# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(lst):
    dict={}
    for element in lst:
        if element in dict:
            dict[element]+= 1
        else:
            dict[element]=1
    highest_count=0
    most_frequent=None

    for element in dict:
        if dict[element]>highest_count:
            highest_count=dict[element]
            most_frequent=element
    
    return most_frequent
