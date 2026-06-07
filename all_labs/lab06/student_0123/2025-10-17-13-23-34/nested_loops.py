# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(f"{i} {j}")
    return full_names

