# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
full_names = []
def get_names(first_names, last_names):
    for f in first_names:
        for l in last_names:
            x = (f + " " + l)
            full_names.append(x)
    return full_names
print(get_names(first_names, last_names))

