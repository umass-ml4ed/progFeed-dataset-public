# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first_name in first_names:
        for last_name in last_names:
            new_name = f"{first_name} {last_name}"
            full_names.append(new_name)
    return full_names

def penalty_calc(assignment):
    penalties = ((0, 1), (1, 0.9), (2, 0.75), (3, 0.5))
    for penalty in penalties:
        if penalty[0] == assignment[1]:
            assignment_grade = assignment[0] * penalty[1]
            break
        else:
            assignment_grade = 0
    return assignment_grade

def average_scores(list_of_scores):
    scores = []
    for student in list_of_scores:
        student_score = 0
        for assignment in student:
            assignment_grade = penalty_calc(assignment)
            student_score += assignment_grade
        scores.append(student_score / len(student))
    return scores

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))