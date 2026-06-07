# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def longest_zigzag_from_start(lst):
    if len(lst)<2:
        return len(lst)
    length = 1

    for i in range(1, len(lst)):
        if i ==1:
            if lst[i]!=lst[i-1]:
                length+=1
                prev_diff = lst[i]-lst[i-1]
            else:
                return length
            
        else:
            current_diff = lst[i]-lst[i-1]
            if current_diff * prev_diff < 0:
                length+=1
                prev_diff = current_diff
            else:
                return length
    return length

#print(longest_zigzag_from_start([1, 3, 2, 4, 3]))

def zigzag_lengths_from_all_starts(lst):
    def get_length(lis, start_index):
        n=len(lis)
        if start_index >= n:
            return 0
        if start_index == n-1:
            return 1
        
        length = 1
        first_diff = lis[start_index+1]-lis[start_index]
        if first_diff == 0:
            return 1
        expected_sign_is_positive = (first_diff > 0)
        
        for i in range(start_index + 1, n - 1):
            current_diff = lis[i + 1] - lis[i]
            if current_diff == 0:
                break
            
            current_sign_is_positive = (current_diff > 0)
            
            if current_sign_is_positive != expected_sign_is_positive:
                length += 1
                expected_sign_is_positive = not expected_sign_is_positive
            else:
                break
                
        return length + 1

    result = []
    for i in range(len(lst)):
        result.append(get_length(lst, i))
    return result

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))