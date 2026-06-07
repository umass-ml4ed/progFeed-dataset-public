#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_zigzag(list_of_integers: list) -> bool:
    if len(list_of_integers) < 3:
        return True
    for n in range(1, (len(list_of_integers)-1)):
        if list_of_integers[n] < list_of_integers[n-1] and list_of_integers[n] < list_of_integers[n+1]:
            continue
        elif list_of_integers[n] > list_of_integers[n-1] and list_of_integers[n] > list_of_integers[n+1]:
            continue
        else:
            return False
    return True


