# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_zigzag(lis_num):

    for num in lis_num:
        if len(lis_num) >= 3:
            if num != lis_num[0] and num != lis_num[-1]:
                if (num <= lis_num[lis_num.index(num)-1] and num >= lis_num[lis_num.index(num)+1]) or ((num >= lis_num[lis_num.index(num)-1] and num <= lis_num[lis_num.index(num)+1])):
                    return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))
print(is_zigzag([1, 4, 2, 5, 3]))
print(is_zigzag([1, 2, 3, 4])) 
print(is_zigzag([10]))
print(is_zigzag([1, 3, 2, 4, 5]))