# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            full_names.append((first_names[i] + " " + last_names[j]))
    return full_names

#print(get_names(["Gavin","Kevin", "Sean"], ["Smith","OLeary"]))