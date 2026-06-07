# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#1. 
def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    length = 1  # A list of fewer than 2 elements counts as a zigzag of length equal to the list length
    i = 0
    
    # The first valid direction:
    if i < len(lst) - 1 and lst[i] == lst[i + 1]:
        i += 1
    
    if i >= len(lst) - 1:
        return length
    
    # The initial direction:
     # 1 is for up, -1 is for down
    direction_sign  = 1 if lst[i] < lst[i + 1] else -1 
    length = 2  # A list of fewer than 2 elements counts as a zigzag of length equal to the list length
    
    # The different valid direction:
    for j in range(i + 1, len(lst) - 1):
        different = lst[j + 1] - lst[j]
        
        if different  == 0:
            # Differences of 0 break the zigzag
            break
        elif (direction_sign  == 1 and different  < 0) or (direction_sign  == -1 and different  > 0):
            direction_sign  *= -1
            length += 1
        else:
            # Invalid 
            break
    
    return length


print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag

print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)

print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start

print(longest_zigzag_from_start([10]))  # 1 → single element

print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start


#2.

def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    if n == 0:
        return []
    
    result = []
    
    for i in range(n):
        if i == n - 1:
            result.append(1)
            continue

        # when len= 1, current= += i:    
        length = 1  
        current = i
        
        # The first valid direction:
        if current < n - 1 and lst[current] == lst[current + 1]:
            current += 1
        
        if current >= n - 1:
            result.append(1)
            continue
            
        # The initial direction:
        if lst[current] < lst[current + 1]:
            direction_sign  = "up"
        else:
            direction_sign  = "down"
        
        # when len= 2, current= += 1:

        length = 2  # A list of fewer than 2 elements counts as a zigzag of length equal to the list length
        current += 1
        
        # check the different direction: 
        while current < n - 1:
            different = lst[current + 1] - lst[current]
            
            if different == 0:
                # Differences of 0 break the zigzag
                break
            elif direction_sign  == "up" and different  < 0:
                # up - down
                direction_sign  = "down"
                length += 1
                current += 1
            elif direction_sign  == "down" and different > 0:
                # down - up 
                direction_sign = "up"
                length += 1
                current += 1
            else:
                #invalid
                break
        
        result.append(length)
    
    return result


print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]
