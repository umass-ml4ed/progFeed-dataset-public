# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names: list, last_names: list) -> list:
    full_names = []
    for i in first_names:
        for j in last_names:
            fullname = i + ' ' + j
            full_names.append(fullname)
    return full_names

def average_scores(List: list) -> list:
    average_grades = []
    assignment_grades = []
    for i in List:
        assignment_grades = []
        for j in i:
            lateness = [0,1,2,3,4,5,6,7,8,9,10]
            percentages = [100,90,75,50,0,0,0,0,0,0,0]
            percent = percentages[lateness.index(j[1])]
            assignment_score = j[0]*percent/100
            assignment_grades.append(assignment_score)
            average = sum(assignment_grades)/len(assignment_grades)
        average_grades.append(average)
    return average_grades


scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))