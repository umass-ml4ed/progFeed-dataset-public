# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    #first_names = ['Ari', 'Taylor']
    #last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
    full_names = []

    for first in range(len(first_names)):
        for last in range(len(last_names)):
            full_names.append(f'{first} {last}')
    return full_names
