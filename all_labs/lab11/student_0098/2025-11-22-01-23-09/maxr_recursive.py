
# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED






def max_recursive(lst): if not lst: return 0 el
if len(lst) == 1: return lst[0] else: return max(lst[0], max_recursive(lst[1:]))
