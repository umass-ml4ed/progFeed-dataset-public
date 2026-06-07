# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def combine_lists(a, b):
        list1 = []
        list2 = []
        list1 = a 
        list2 = b
        num = len(b)
        num1 = int((len(a)) / 2)
        list1.insert(list2[0],0)
        list1.append(list2[(num - 1)])
        list1.pop(num1)


        return list1

def classify_by_length(a):
        if len(a) == 0:
                return "empty"
        elif int((len(a))%2) == 0:
                return "even_length"
        else:
                return "odd_length"
print(classify_by_length([1,2,3]))


        


