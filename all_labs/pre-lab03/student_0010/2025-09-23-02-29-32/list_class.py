# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def combine_lists(a, b):
        num = len(b)
        num1 = int((len(a)) / 2)
        a.insert(0, b[0])
        a.append(b[(num - 1)])
        a.pop(len(a) // 2)
        return a

def classify_by_length(a):
        if len(a) == 0:
                return "empty"
        elif int((len(a))%2) == 0:
                return "even_length"
        else:
                return "odd_length"
print(classify_by_length([1,2,3]))


        


