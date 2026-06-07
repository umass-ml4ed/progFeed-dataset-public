# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor' ]
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first_names, last_names):
    full_name = []
    for first in first_names:
        for last in last_names:
            full_names= (f"{first} {last}")
            full_name.append(full_names)
    return full_name
    

print(get_names(first_names, last_names))