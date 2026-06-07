# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names,last_names):
    full_names = []
    for i in range(len(first_names)):
        full = first_names[i] + " " + last_names[i]
        full_names.append(full)
    return full_names
