# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def is_zigzag(l:list) -> bool:
        z = True
        for i in range(1,len(l)-1):
            if (l[i-1] < l[i] and l[i] > l[i+1]) or (l[i-1] > l[i] and l[i] < l[i+1]):
                continue
            else:
                z = False
                return z
        return z

