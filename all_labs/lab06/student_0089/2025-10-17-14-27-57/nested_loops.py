# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in range(0, len(first_names)):
        for j in range(0, len(last_names)):
            full_names.append(str(first_names[i]) + " " + str(last_names[j]) + ", ") # i only index. # first_names[i] = values
    return full_names

first_name = ['Ari', 'Taylor']
last_name = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_name, last_name))


