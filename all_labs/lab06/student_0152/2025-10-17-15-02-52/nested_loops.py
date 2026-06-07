# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
           full_names.append(first + " " + last)
    return full_names

def average_scores(list):
    final_list = []
    for scores in list:
        total = 0
        assignments = 0
        for grade, lateness in scores:
            if lateness == 0:
                late_grade = grade * 1.0
            elif lateness == 1:
                late_grade = grade * 0.90
            elif lateness == 2:
                late_grade = grade * 0.75
            elif lateness == 3:
                late_grade = grade * 0.50
            else:
                late_grade = 0.0
            total += late_grade
            assignments += 1
        if assignments > 0:
            average = total / assignments
            final_list.append(average)
        else:
            final_list.append(0)
    return final_list