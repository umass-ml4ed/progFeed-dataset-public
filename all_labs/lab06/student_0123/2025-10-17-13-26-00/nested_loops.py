# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(f"{i} {j}")
    return full_names

def average_scores(lst):
    penalties = {0: 1.00, 1: 0.90, 2: 0.75, 3: 0.50}
    results = []
    for student in lst:
        total = 0
        count = 0
        for grade, lateness in student:
            if lateness >= 4:
                adjusted = 0
            else:
                adjusted = grade * penalties.get(lateness, 0)
            total += adjusted
            count += 1
        average = total / count if count > 0 else 0
        results.append(average)
    return results