# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

full_names = []
def get_names (first_names, last_names):
    for f in first_names:
        for l in last_names:
            full_names.append(f + ' ' + l)
    return(full_names)


#print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))

