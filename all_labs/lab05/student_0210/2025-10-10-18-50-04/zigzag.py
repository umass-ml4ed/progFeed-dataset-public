# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(List):
    if len(List) < 3:
        return True
    for i in range(1, len(List) - 1):
        if not ((List[i] > List[i - 1] and List[i] > List[i + 1]) or (List[i] < List[i - 1] and List[i] < List[i + 1])):
            return False
    return True