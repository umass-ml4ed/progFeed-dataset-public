# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def get_names(first_names: list, last_names: list):
    full_names = []
    for fname in first_names:
        for lname in last_names:
            full_names.append(f"{fname} {lname}")
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names, last_names))
