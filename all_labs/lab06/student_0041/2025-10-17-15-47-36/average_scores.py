# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def average_scores(scores):
    final_grade = []
    for student in scores:
        # student [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)]
        sum_grades = 0
        for assignment in student:
            # assignment (90, 0)
            grade = assignment[0]
            lateness = assignment[1]
            #sum_grades = 0
            if lateness == 0:
                sum_grades += grade
                #break
            elif lateness == 1:
                sum_grades += grade*0.9
                #break
            elif lateness == 2:
                sum_grades += grade*0.75
                #break
            elif lateness == 3:
                sum_grades += grade*0.50
                #break
            else:
                sum_grades += grade*0
                #break

        average = sum_grades / len(student)
        final_grade.append(average)

    return final_grade

print(average_scores(scores))