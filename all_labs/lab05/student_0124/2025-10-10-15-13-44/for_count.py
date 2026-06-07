# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def count_strings(lof:list, n:int) -> int:
    count = 0
    for i in range(len(lof)):
        if n == len(lof[i]):
            count += 1
    return count

