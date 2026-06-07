#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def get_names(first, last):
    full_names = []
    for i in first:
        for x in last:
            full_names.append(i + " " + x)
    return full_names
        
print (get_names(['Ari', 'Taylor'],['Levine', 'Lopez', 'Khan', 'Wang']))