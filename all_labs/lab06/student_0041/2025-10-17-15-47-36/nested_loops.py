# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            format = str(i) + " " + str(j)
            full_names.append(format)
    return full_names

print(get_names(first_names, last_names))