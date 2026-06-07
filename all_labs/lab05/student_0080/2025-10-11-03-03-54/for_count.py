# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strings, n):
    count = 0
    for string in strings:
        if len(string) >= n:
            count += 1
    return count

if __name__ == "__main__":
    print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # 4
    print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # 2
    print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # 0
    print(count_strings([], 5))                       # 0 (edge case: empty list)
    print(count_strings(['hello', 'world'], 10))      # 0 (edge case: large n)