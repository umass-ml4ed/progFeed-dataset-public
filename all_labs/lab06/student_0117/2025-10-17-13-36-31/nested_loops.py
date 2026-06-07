# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for names in first_names:
        for l_names in last_names:
            full_names.append(f'{names} {l_names}')
    return full_names

def average_scores(out_lst):
    average_grades = []
    for students in out_lst:
        student_average = 0
        net_assignment_grade = 0
        for assignment in students:
            if assignment[1] == 0:
                net_assignment_grade += assignment[0]
            if assignment[1] == 1:
                net_assignment_grade += assignment[0]*.9
            if assignment[1] == 2:
                net_assignment_grade += assignment[0]*.75
            if assignment[1] == 3:
                net_assignment_grade += assignment[0]*.5
            if assignment[1] == 4:
                net_assignment_grade += 0
        student_average = net_assignment_grade/(len(students))
        average_grades.append(student_average)
    return average_grades
