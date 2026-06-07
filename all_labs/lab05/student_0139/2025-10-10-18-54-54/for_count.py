def count_strings(l1,n):
    a=0
    for i in l1:
        if len(i)>=n:
            a+=1
    return(a)
    
count_strings(['', 'a', 'aa', 'aaa'], 0)   # should return 4
count_strings(['', 'a', 'aa', 'aaa'], 2)   # should return 2 
count_strings(['', 'a', 'aa', 'aaa'], 4)   # should return 0

