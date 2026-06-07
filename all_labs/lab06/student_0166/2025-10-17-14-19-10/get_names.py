# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_name, last_name):
    full_names=[]
    for a in first_name:
        for b in last_name:
            combined_names = a + " " + b
            full_names.append(combined_names)
    return full_names
