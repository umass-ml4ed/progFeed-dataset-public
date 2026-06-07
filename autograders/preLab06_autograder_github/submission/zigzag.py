def longest_zigzag_from_start(lst):
    """Return the length of the longest zigzag starting from the first element."""
    n = len(lst)
    if n < 2:
        return n

    length = 1
    prev_diff = 0

    for i in range(1, n):
        diff = lst[i] - lst[i-1]
        if diff == 0:
            break  # cannot continue if difference is 0
        if prev_diff == 0 or diff * prev_diff < 0:
            length += 1
            prev_diff = diff
        else:
            break  # zigzag breaks

    return length
# zigzag_lengths_from_all_starts.py

def zigzag_lengths_from_all_starts(lst):
    """Return a list of lengths of the longest zigzag subarray starting at each position."""
    n = len(lst)
    if n == 0:
        return []

    lengths = [1] * n  # at least length 1 for each start

    for start in range(n):
        prev_diff = 0
        curr_len = 1
        for i in range(start+1, n):
            diff = lst[i] - lst[i-1]
            if diff == 0:
                break
            if prev_diff == 0 or diff * prev_diff < 0:
                curr_len += 1
                prev_diff = diff
            else:
                break
        lengths[start] = curr_len

    return lengths

# Example runs
if __name__ == "__main__":
    print(longest_zigzag_from_start([1, 3, 2, 4, 3]))        # 5
    print(longest_zigzag_from_start([1, 2, 3, 4, 5]))        # 2
    print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))     # 5
    print(longest_zigzag_from_start([10]))                   # 1
    print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3

    print("Testing zigzag_lengths_from_all_starts...")
    print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))        # [5, 4, 3, 2, 1]
    print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))        # [2, 2, 2, 2, 1]
    print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))     # [5, 4, 3, 2, 2, 1]
    print(zigzag_lengths_from_all_starts([10]))                   # [1]
    print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3, 0, 5, 7, 6, 8, 7]))  # [3, 3, 2, 2, 2, 2, 1]
