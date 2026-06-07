def filter_positive(nums):
    pos_nums = []
    for i in nums:
        if i>0:
            pos_nums.append(i)
    return pos_nums