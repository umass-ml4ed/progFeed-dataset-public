# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names,last_names):
    full_names=[]
    for name in first_names:
        for name2 in last_names:
            full_name = name + ' ' + name2
            full_names.append(full_name)
    return full_names



