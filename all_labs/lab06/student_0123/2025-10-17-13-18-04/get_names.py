# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    x = (len(first_names) -1) * (len(last_names) - 1)
    y = len(first_names) - 1
    z = len(last_names) - 1
    while y >= 0:
        full_names.append(first_names[y] + " " + last_names[z])
        z -= 1
        if y >= 0 and z < 0:
            y -= 1
            z = len(last_names) - 1
    return full_names

            
