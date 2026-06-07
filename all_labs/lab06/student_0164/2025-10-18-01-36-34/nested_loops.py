# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            full_name = first_names[i] + " " + last_names[j]
            full_names.append(full_name)

    return full_names 
        


first_names = ['Ari']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names, last_names))







