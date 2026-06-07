def filter_positive(lis):
    result = []
    for num in lis:
        if(num > 0):
            result.append(num)
        num += 1
    return result

print(filter_positive([1, -3, 5, 0, -2, 7]))