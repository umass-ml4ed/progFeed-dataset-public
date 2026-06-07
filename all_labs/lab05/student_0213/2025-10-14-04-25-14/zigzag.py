# Name     : REDACTED_NAME
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(listy):
    n = len(listy)
    i = 0
    if n < 3:
        return True
    for i in range(1, n - 1):
        if (listy[i] > listy[i - 1] and listy[i] > listy[i + 1]) or (listy[i] < listy[i - 1] and listy[i] < listy[i + 1]):
            i += 1
            continue
        else:
            return False
    while i == (n - 1):
        return True
    
print(is_zigzag([7, 9, 6, 15, 1, 1006, 522, 707, 706, 1004, 995, 60789, 5143, 78888]))