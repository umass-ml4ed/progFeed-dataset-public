def count_strings(lst, length):
    count = 0
    for s in lst:
        if len(s) >= length:
            count += 1
    return count
