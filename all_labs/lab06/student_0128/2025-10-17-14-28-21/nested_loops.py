# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names, last_names):
    full_names = []
    for f in first_names:
        for l in last_names:
            full_names.append(f + ' ' + l)
    return full_names

def average_scores(scores_lateness):
    final_averages = []
    for student in scores_lateness:
        sum = 0
        for assignments in student:
            if assignments[1] == 0:
                sum += assignments[0]
            elif assignments[1] == 1:
                sum += (assignments[0] * 0.90)
            elif assignments[1] == 2:
                sum += (assignments[0] * 0.75)
            elif assignments[1] == 3:
                sum += (assignments[0] * 0.50)
        final_averages.append(sum / len(student))
    return final_averages