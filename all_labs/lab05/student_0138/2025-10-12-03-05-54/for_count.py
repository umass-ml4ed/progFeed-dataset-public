# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def count_strings(lis, n):
    count = 0
    for chr in lis:
        if len(chr) >= n:
            count += 1
    return count

print(count_strings(['', 'a', 'aa', 'aaa'], 0))


