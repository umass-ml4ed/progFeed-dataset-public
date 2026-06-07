# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

#combine_lists

def combine_lists(a, b):
   
    a.insert(0, b[0])
    a.append(b[-1])
    middle_a = len(a) // 2
    a.pop(middle_a)

    return a

#classify_by_length

def classify_by_length(a):
    if len(a) == 0:
       return "empty"
    elif len(a) % 2 == 0: 
        return "even_length"
    else:
       return "odd_length"
    




#print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
#print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))


print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))
