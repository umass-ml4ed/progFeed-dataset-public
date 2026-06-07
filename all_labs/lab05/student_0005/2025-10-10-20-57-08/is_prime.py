def nums():
    sum = 0
    for n in range(1, 100, 2):
        sum += n
        if sum >= 20:
            break

print(nums)