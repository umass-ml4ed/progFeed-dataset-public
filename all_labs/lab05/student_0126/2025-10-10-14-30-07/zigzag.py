# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(a):
    for i in range(1, len(a) - 1):
        if not (((int(a[i]) > int(a[i + 1])) and (int(a[i]) > int(a[i - 1]))) or ((int(a[i]) < int(a[i + 1])) and (int(a[i]) < int(a[i - 1])))):
            return False
    return True


