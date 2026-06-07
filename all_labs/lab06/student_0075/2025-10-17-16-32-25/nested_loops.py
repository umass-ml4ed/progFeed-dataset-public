# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ["Gavin", "Kevin", "David", "Steve"]
last_names = ["O'Leary", "Smith", "Cruz", "Rios"]
full_names = []


def get_names(first_names,last_names):
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            full_names.append((first_names[i], last_names[j]))
    return full_names

print(get_names(first_names, last_names))