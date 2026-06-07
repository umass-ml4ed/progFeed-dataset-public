# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(f"{i} {j}")
    return full_names
def average_scores(scores):
    lst = []
    for i in scores:
        edit = 0
        for grade, lateness in i:
            if lateness == 0:
                multiplier = 1
            elif lateness == 1:
                multiplier = 0.9
            elif lateness == 2:
                multiplier = 0.75
            elif lateness == 3:
                multiplier = 0.5
            elif lateness >= 4:
                multiplier = 0
            edit = edit + grade * multiplier
        lst.append(edit / len(i))
    return lst