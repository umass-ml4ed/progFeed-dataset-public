# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def combine_lists(alist,blist):
    alist.insert(0, blist[0])
  
    alist.append(blist[len(blist)-1]) 
    middleindex= int(len(alist)/2)
    alist.pop(middleindex)
    return alist
# Uncomment the following lines (remove the # characters on each line)
# to test combine_lists()
print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))

def classify_by_length(a):
    if a==[]:
        return "empty"
    elif len(a)%2==0:
        return "even_length"
    else:
        return "odd_length"
    
# Uncomment the following lines (remove the # characters on each line)
# to test classify_by_length()
print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))

