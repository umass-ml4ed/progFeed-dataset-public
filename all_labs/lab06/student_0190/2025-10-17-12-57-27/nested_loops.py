# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']


def get_names(first, last):
    result = []
    for f in first:
        for l in last:
            result.append(f + " " + l)
    return result

print(get_names(first_names, last_names))