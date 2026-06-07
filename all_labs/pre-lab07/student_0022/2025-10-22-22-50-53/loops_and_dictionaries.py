# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    current_n = n
    output = ""
    while current_n > 0:
        nums = ""
        for value in range(current_n):
            if current_n-value > 0:
                nums += str(current_n-value) + " "
        if nums == "1":
            output += nums
        else:
            output += nums+"\n"
        current_n -= 1
    return output
 
def merge_dicts(d1,d2):
    new_dict = d1.copy()
    for key in d2:
        if key in d1:
            new_dict[key] = d1[key] + d2[key]
        else:
            new_dict[key] = d2[key]
    return new_dict

print(pyramid(4))