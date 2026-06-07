# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    count = 1
    prev_diff = 0

    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]

        if diff == 0:
            break

        if prev_diff == 0 or (diff > 0 and prev_diff < 0) or (diff < 0 and prev_diff > 0):
            count += 1
            prev_diff = diff
        else:
            break

    return count

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))