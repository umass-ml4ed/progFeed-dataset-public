# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names, last_names):
    full_names = []
    
    for first in first_names:
        for last in last_names:
            full_name = first + " " + last
            full_names.append(full_name)

    return full_names


first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

result = get_names(first_names, last_names)
print(result)


def average_scores(scores):
    #function to help apply the lateness penalties
    def apply_penalty(lateness):
        if lateness == 0:
            return 1.0
        elif lateness == 1:
            return 0.9
        elif lateness == 2:
            return 0.75
        elif lateness == 3:
            return 0.5
        else:
            return 0

    average_scores_list = []

    for student_scores in scores:
        total_score = 0
        total_weighted_score = 0
        num_assignments = len(student_scores)
        
        for grade, lateness in student_scores:
            penalty = apply_penalty(lateness)
            total_weighted_score += grade * penalty
        
        average_score = total_weighted_score / num_assignments
        average_scores_list.append(average_score)

    return average_scores_list

scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(average_scores(scores))
