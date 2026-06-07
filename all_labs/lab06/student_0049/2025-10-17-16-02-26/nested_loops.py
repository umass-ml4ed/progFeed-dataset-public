# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_nam, last_nam):
    full_name = []
    for i in first_nam:
        for k in last_nam:
            full_name.append(i + ' ' + k)
    return full_name

def average_scores(scores):
    average = []
    for i in scores:
        total = 0
        for grade, lateness in i:
            if lateness == 0:
                mult = 1.0
            elif lateness == 1:
                mult = 0.9
            elif lateness == 2:
                mult = 0.75
            elif lateness == 3:
                mult = 0.5
            else:
                mult = 0
            total += grade * mult
        avg = total / len(i)
        average.append(avg)
    return average
