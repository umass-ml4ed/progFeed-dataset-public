def filter_positive(nums):
    positives = []
    for num in nums:
        if num > 0:
            positives.append(num)
    return positives



print("Testing filter_positive...")
print(filter_positive([1, -3, 5, 0, -2, 7]))   # [1, 5, 7]
print(filter_positive([-5, -1, -10]))          # []
print(filter_positive([10, 20, -30, 40]))      # [10, 20, 40])