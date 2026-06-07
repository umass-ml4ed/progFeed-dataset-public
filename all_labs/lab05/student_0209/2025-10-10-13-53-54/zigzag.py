


# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




def is_zigzag(n_list):
    if len(n_list) < 2:
        return True
    for i in range(1, len(n_list)-1):
        if not ((n_list[i] > n_list[i-1] and n_list[i] > n_list[i+1]) or (n_list[i] < n_list[i-1] and n_list[i] < n_list[i+1])):
            return False
    return True



    