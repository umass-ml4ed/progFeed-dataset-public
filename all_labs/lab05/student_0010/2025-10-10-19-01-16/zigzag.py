# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
                        


      
def is_zigzag(num_list):
    if len(num_list) < 2:
        return True

    dif = num_list[1] - num_list[0]
    if dif == 0:
        return False

    for i in range(2, len(num_list)):
        ndif = num_list[i] - num_list[i-1]
        
        if dif * ndif >= 0:
            return False 

    return True