# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names



def average_scores(scores):
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}  

    result = []
    for student in scores:
        total = 0
        for grade, late in student:
            if late >= 4:
                total += 0
            else:
                total += grade * penalties.get(late, 0)
        avg = total / len(student)
        result.append(avg)
    return result

