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
        if prev_diff == 0:
            count += 1
            prev_diff = diff
        else:
            if prev_diff * diff < 0:
                count += 1
                prev_diff = diff
            else:
                break

    return count


def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    if n == 0:
        return []

    result = [0] * n
    for start in range(n):
        if start == n - 1:
            result[start] = 1
            continue

        count = 1
        prev_diff = 0
        for i in range(start + 1, n):
            diff = lst[i] - lst[i - 1]
            if diff == 0:
                break
            if prev_diff == 0:
                count += 1
                prev_diff = diff
            else:
                if prev_diff * diff < 0:
                    count += 1
                    prev_diff = diff
                else:
                    break

        result[start] = count

    return result

