# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list, n):
  count = 0
  for s in list:
    if len(s) >= n:
      count += 1
  return count
