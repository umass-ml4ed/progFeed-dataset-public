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

        for grade, late in s:  
            if late == 0:
                multiply = 1.0
            elif late == 1:
                multiply = 0.9
            elif late == 2:
                multiply = 0.75
            elif late == 3:
                multiply = 0.5
            else:  
                multiply = 0.0

            total += grade * multiply
        average = total / len(s)
        results.append(average)

    return results