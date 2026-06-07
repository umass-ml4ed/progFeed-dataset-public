def count_strings(s,n):
    count = 0
    for x in s:
        if(len(x)>=n):
            count+= 1
    return count