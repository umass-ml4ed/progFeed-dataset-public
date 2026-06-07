
# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# nested_loops

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_name = first + " " + last
            full_names.append(full_name)
    return full_names

def average_scores(scores):
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}
    averages = []

    for student in scores:
        total = 0
        for grade, lateness in student:
            # Apply lateness penalty
            if lateness >= 4:
                effective_score = 0
            else:
                effective_score = grade * penalties[lateness]
            total += effective_score
        # Compute average for each student
        avg = total / len(student)
        averages.append(avg)

    return averages