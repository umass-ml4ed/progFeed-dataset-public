# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(fn, ln):
    names = []
    for firstname in fn:
        for lastname in ln:
            names.append(f'{firstname} {lastname}')
    return names

print(get_names(fn, ln))


