# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names,last_names):
    full_names = []
    for f in first_names:
        for l in last_names:
            full_names.append(f"{f} {l}")
    return full_names
