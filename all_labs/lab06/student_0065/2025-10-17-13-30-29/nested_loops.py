# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names: list, last_names: list):
    
    full_names=[]
    for i in first_names:
        for j in last_names:
            name_combo = i + ' ' + j
            full_names.append(name_combo)
    return full_names

