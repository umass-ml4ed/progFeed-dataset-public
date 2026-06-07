def most_frequent_element(lst):
    if not lst:
        return None
    d = {}
    for item in lst:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    max_item = None
    max_count = 0
    for item in d:
        if d[item] > max_count:
            max_count = d[item]
            max_item = item
    return max_item

