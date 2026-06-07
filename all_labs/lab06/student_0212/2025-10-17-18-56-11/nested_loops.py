# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first_name in first_names:
        for last_name in last_names:
            full_names.append(f"{first_name} {last_name}")
    return full_names

def average_scores(students_scores):
    average_scores_list = []
    for student in students_scores:
        total_scores = 0
        assignment_count = 0
        for assignment in student:
            if assignment[1] == 0:
                score = assignment[0]
            elif assignment[1] == 1:
                score = 0.9 * assignment[0]
            elif assignment[1] == 2:
                score = 0.75 * assignment[0]
            elif assignment[1] == 3:
                score = 0.5 * assignment[0]
            elif assignment[1] == 4:
                score = 0
            total_scores += score
            assignment_count += 1
        average_scores_list.append(total_scores / assignment_count)
    return average_scores_list

