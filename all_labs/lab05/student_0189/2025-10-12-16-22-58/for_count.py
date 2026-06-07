# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strings, n):
    count = 0
    for s in strings:
        if len(s) >= n:
            count += 1
    return count

assert count_strings(['', 'a', 'aa', 'aaa'], 0) == 4
assert count_strings(['', 'a', 'aa', 'aaa'], 2) == 2
assert count_strings(['', 'a', 'aa', 'aaa'], 4) == 0

assert count_strings([], 0) == 0
assert count_strings([], 5) == 0
assert count_strings(['x', 'yy', 'zzz'], 1) == 3
assert count_strings(['x', 'yy', 'zzz'], 2) == 2
assert count_strings(['x', 'yy', 'zzz'], 3) == 1
assert count_strings(['', '', ''], 0) == 3
assert count_strings(['', '', ''], 1) == 0
assert count_strings(['abc'], -1) == 1
assert count_strings(['a'*1000, 'b'*500], 800) == 1