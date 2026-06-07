# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names,last_names):
    full_names = []
    for f in first_names:
        for l in last_names:
            full_names.append(f"{f} {l}")
    return full_names

def average_scores(scores):
    results = []
    for s in scores:  
        total = 0

        for grade, lateness in s:  
            if lateness == 0:
                multiply = 1.0
            elif lateness == 1:
                multiply = 0.9
            elif lateness == 2:
                multiply = 0.75
            elif lateness == 3:
                multiply = 0.5
            else:  
                multiply = 0.0

            total += grade * multiplier
        average = total / len(s)
        results.append(average)

    return results