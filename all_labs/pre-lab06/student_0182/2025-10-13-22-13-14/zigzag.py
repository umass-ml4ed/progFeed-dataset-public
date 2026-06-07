# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    """Return the length of the longest zigzag subsequence starting at index 0."""
    n = len(lst)
    if n < 2:
        return n

    length = 1
    last_diff = 0  

    for i in range(1, n):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break  
        if last_diff == 0:
            length += 1
            last_diff = 1 if diff > 0 else -1
        elif (diff > 0 and last_diff < 0) or (diff < 0 and last_diff > 0):
            length += 1
            last_diff = 1 if diff > 0 else -1
        else:
            break  
    return length


def zigzag_lengths_from_all_starts(lst):
    """Return a list where each element i is the length of the longest zigzag starting at i."""
    n = len(lst)
    if n == 0:
        return []
    if n == 1:
        return [1]

    result = []
    for start in range(n):
        if start == n - 1:
            result.append(1)
            continue
        length = 1
        last_diff = 0
        for i in range(start + 1, n):
            diff = lst[i] - lst[i - 1]
            if diff == 0:
                break
            if last_diff == 0:
                length += 1
                last_diff = 1 if diff > 0 else -1
            elif (diff > 0 and last_diff < 0) or (diff < 0 and last_diff > 0):
                length += 1
                last_diff = 1 if diff > 0 else -1
            else:
                break
        result.append(length)
    return result



if __name__ == "__main__":
    print(longest_zigzag_from_start([1, 3, 2, 4, 3]))      
    print(longest_zigzag_from_start([1, 2, 3, 4, 5]))      
    print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))   
    print(longest_zigzag_from_start([10]))                 
    print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))

    print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))   
    print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))   
    print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))
    print(zigzag_lengths_from_all_starts([10]))              
