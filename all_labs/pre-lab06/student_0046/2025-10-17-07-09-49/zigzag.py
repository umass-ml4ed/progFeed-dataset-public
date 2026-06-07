# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from typing import List

def longest_zigzag_from_start(lst: List[int]) -> int:
    """Return the length of the longest contiguous zigzag subsequence
    that *starts at index 0*.
    A zigzag alternates strictly up/down in consecutive differences.
    Differences of 0 break the zigzag.
    """
    n = len(lst)
    if n < 2:
        return n

    # Find the first nonzero difference to set initial direction.
    i = 1
    while i < n and lst[i] - lst[i - 1] == 0:
        # zeros break immediately: the best we can do is length 1
        return 1
    if i >= n:
        return 1  # all equal elements
    diff = lst[i] - lst[i - 1]
    if diff == 0:
        return 1
    sign = 1 if diff > 0 else -1
    length = 2  # so far lst[0]..lst[i]

    # Continue while the sign strictly alternates and diffs are nonzero.
    for j in range(i + 1, n):
        d = lst[j] - lst[j - 1]
        if d == 0:
            break
        s = 1 if d > 0 else -1
        if s == -sign:
            length += 1
            sign = s
        else:
            break
    return length


def zigzag_lengths_from_all_starts(lst: List[int]) -> List[int]:
    """For each start index i, return the length of the longest
    contiguous zigzag subsequence starting at i.
    This implementation purposefully uses nested loops (as the lab topic).
    """
    n = len(lst)
    if n == 0:
        return []
    ans = [1] * n
    for i in range(n):
        # extend from i forward while the sign alternates
        if i == n - 1:
            ans[i] = 1
            continue
        # determine initial direction
        d = lst[i + 1] - lst[i]
        if d == 0:
            ans[i] = 1
            continue
        sign = 1 if d > 0 else -1
        length = 2
        # inner loop: grow the zigzag from i
        for j in range(i + 2, n):
            step = lst[j] - lst[j - 1]
            if step == 0:
                break
            s = 1 if step > 0 else -1
            if s == -sign:
                length += 1
                sign = s
            else:
                break
        ans[i] = length
    return ans