# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(list_of_integers: list):
    if len(list_of_integers) < 3:
        return True
    for i in range(1, len(list_of_integers) - 1):
        if not ((list_of_integers[i] > list_of_integers[i - 1] and list_of_integers[i] > list_of_integers[i + 1]) or
                (list_of_integers[i] < list_of_integers[i - 1] and list_of_integers[i] < list_of_integers[i + 1])):
            return False
    return True

            
