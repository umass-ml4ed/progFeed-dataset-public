# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(f_names, l_names):
    full_names = []
    for first in f_names:
        for last in l_names:
            full_names.append(first + " " + last)
    return full_names

def average_scores(grade, lateness):
    averages = []
    for g in grade:
        for l in lateness:
            avg = g - (l * 2)
            if avg < 0:
                avg = 0
            averages.append(avg)
    return averages