def count_strings(strings, n):
    count = 0
    for s in strings:
        if len(s) >= n:
            count += 1
    return count


print(count_strings(['', 'a', 'aa', 'aaa'], 0))  # Expected output: 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))  # Expected output: 2
print(count_strings(['', 'a', 'aa', 'aaa'], 4))  # Expected output: 0
