# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for k in last_names:
            full_names.append(f"{i} {k}")
    return full_names

def average_scores(scores):
    averages = []
    for j in scores:
        total = 0
        for grade, lateness in j:
            if lateness == 0:
                total += grade
            elif lateness == 1:
                total += grade * 0.9
            elif lateness == 2:
                total += grade * 0.75
            elif lateness == 3:
                total += grade * 0.5
            else:
                total += 0
        averages.append(total / len(j))
    return averages


