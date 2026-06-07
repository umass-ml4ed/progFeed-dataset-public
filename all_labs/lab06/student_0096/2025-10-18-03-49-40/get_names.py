# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names, last_names):
    full_names = [] 

    for first in first_names:          
        for last in last_names:        
            full_name = first + " " + last
            full_names.append(full_name)

    return full_names




