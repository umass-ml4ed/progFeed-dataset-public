def count_strings(list_1,n):
    count=0
    for s in list_1:
        if len(s)>=n:
            count=count+1
    return count
