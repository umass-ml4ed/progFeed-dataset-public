# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(FName, LName):
    full_names = []
    for first in FName:
        for last in LName:
            full_names.append(f"{first} {last}")
    return full_names

def average_scores(all_scores):
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}
    avrage = []
    for studentScores in all_scores:
        total = 0
        for grade, lateness in studentScores:
            if lateness >= 4:
                x = 0
            else:
                x = grade * penalties[lateness]
            total += x
        avg = total / len(studentScores)
        avrage.append(avg)
    return avrage