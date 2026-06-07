# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def  get_names(first_names, last_names): 
    full_names = [] 
    new_name = ""
    for k in range(0, len(first_names)): 
        for j in range(0, len(last_names)):
            new_name = first_names[k] + ' ' + last_names[j]
            full_names.append(new_name)
    return full_names 

def average_scores(big_list):
    avg_grade = [] 
    for student in big_list:
        each_student = 0 
        for assignment in student: 
            if assignment[1] == 0:
                each_student += assignment[0]
            elif assignment[1] == 1: 
                each_student += assignment[0] * 0.9
            elif assignment[1] == 2: 
                each_student += assignment[0] * 0.75
            elif assignment[1] == 3: 
                each_student += assignment[0] * 0.5
            elif assignment[1] >= 4: 
                each_student += 0
        avg_grade.append(each_student/len(student))
    return avg_grade 

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))