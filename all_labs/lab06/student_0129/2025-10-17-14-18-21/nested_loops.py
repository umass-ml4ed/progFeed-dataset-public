# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(firsts, lasts):
    names = []
    for first in firsts:
        for last in lasts:
            names.append(first + " " + last)
    return names

def average_scores(scores):
    avrg = []
    for score in scores:
        total = 0
        count = len(score)
        for grade, lateness in score:
            if lateness == 0:
                total += grade * 1.0
            elif lateness == 1:
                total += grade * 0.9
            elif lateness == 2:
                total += grade * 0.75
            elif lateness == 3:
                total += grade * 0.5
            else:
                total += grade * 0.0
        avrg.append(total / count)
    return avrg
