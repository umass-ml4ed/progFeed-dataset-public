#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def get_names(first_names: list, last_names: list) -> list:
    full_names = []
    for fn in first_names:
        for ln in last_names:
            full_names.append(f'{fn} {ln}')
    return full_names

def average_scores(scores) -> list:
    final_scores = []
    for student in scores:
        student_grade = 0
        for assignment in student:
            number_of_assignments = len(student)
            if assignment[1] == 0:
                student_grade += assignment[0]
            elif assignment[1] == 1:
                student_grade += assignment[0] * 0.9
            elif assignment[1] == 2:
                student_grade += assignment[0] * 0.75
            elif assignment[1] == 3:
                student_grade += assignment[0] * 0.5
            elif assignment[1] == 4:
                student_grade += 0
        final_scores.append(student_grade/number_of_assignments)
    return final_scores


scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))
        


