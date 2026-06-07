# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
                        
def is_zigzag(num_list):
    if len(num_list) < 3:
        return True

    for i in range(1, len(num_list) - 1):
        l = num_list[i-1]
        r = num_list[i]
        t = num_list[i+1]

        y = (l < r and r > t)
        u = (l > r and r < t)
        if not (y or u):
            return False
            
    return True
