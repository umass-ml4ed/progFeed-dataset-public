# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
                        
def is_zigzag(num_list):
    if len(num_list) < 2:
        return True

    for i in range(2, len(num_list)):
        i = num_list[i-2]
        r = num_list[i-1]
        t = num_list[i]

        case1 = (i < r and r > t)
        case2 = (i > r and r < t)

        if not (case1 or case2):
            return False

    return True


      
