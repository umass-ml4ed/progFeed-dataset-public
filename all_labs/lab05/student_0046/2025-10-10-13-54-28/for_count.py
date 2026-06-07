# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strings: list[str], n: int) -> int:
    count = 0
    for s in strings:
        if len(s) >= n:
            count += 1
    return count