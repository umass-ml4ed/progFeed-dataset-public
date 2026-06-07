# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
full_names = []


def get_names(first_names, last_names):
    for firstName in first_names:
        for lastName in last_names:
            full_name = firstName + " " + lastName
            full_names.append(full_name)

    return full_names

print(get_names(first_names,last_names))