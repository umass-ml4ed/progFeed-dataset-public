# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(firstnames, lastnames):
    full_names = []
    for fname in firstnames:
        for lname in lastnames:
            combine = fname+" "+lname
            full_names.append(combine)
    return full_names

def average_scores(student_lists):
    average_list = []
    for assignment in student_lists:
        total = 0
        for grades in assignment:
            if grades[1] == 0:
                total = total + grades[0]
            elif grades[1] == 1:
                total = total + grades[0]*0.9
            elif grades[1] == 2:
                total = total + grades[0]*0.75
            elif grades[1] == 3:
                total = total + grades[0]*0.5
        average = total/len(assignment)
        average_list.append(average)
    return average_list

score = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(score))