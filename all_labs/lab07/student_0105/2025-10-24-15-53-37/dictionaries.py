# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(tup):
    emp_dict = {}
    for i in tup:
        if i not in emp_dict:
            emp_dict[i] = 1
        else:
            emp_dict[i] += 1
    return emp_dict

def average_prices(tup):
    emp_dict = {}
    count = {}
    for i in tup:
        if i[0] not in emp_dict:
            emp_dict[i[0]] = i[1]
            count[i[0]] = 1
        else:
            emp_dict[i[0]] += i[1]
            count[i[0]] += 1
    for x in emp_dict:
        emp_dict[x] = emp_dict[x] / count[x]
    return emp_dict

def count_bigrams(tup):
    emp_dict = {}
    lst = []
    for i in range(len(tup)):
        try:
            lst.append((tup[i], tup[i + 1]))   
        except IndexError:
            lst = lst
    for l in range(len(lst)):
       try:
           if (lst[l]) not in emp_dict:
               emp_dict[lst[l]] = 1
           else:
               emp_dict[lst[l]] += 1
       except IndexError:
           emp_dict = emp_dict    
    return emp_dict

words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
print(count_bigrams(words))

    



