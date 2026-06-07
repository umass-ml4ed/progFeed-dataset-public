# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names, last_names):
    combos = []
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            combos.append(first_names[i] + " " + last_names[j])
    return combos


firsts = ['Ari', 'Taylor']
lasts = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(firsts, lasts))
