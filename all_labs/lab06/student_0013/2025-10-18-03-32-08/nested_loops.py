# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names, last_names):
    first_names = ['Ari', 'Taylor']
    last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
    
    for i in range(len(first_names)):
        for j in range(len(last_names)):  
            print(first_names[i] + " " + last_names[j])