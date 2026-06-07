# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_name = i + " " + j
            full_names.append(full_name)

    return full_names

print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))
            

def average_scores(scores):
    average_scores = []
    for assignment in scores:
        adjusted_score = 0
        assignment_count = 0
        for score,lateness in assignment:
            if lateness == 0:
                new_score = score
            elif lateness == 1:
                new_score = score * 0.9
            elif lateness == 2:
                new_score = score * 0.75
            elif lateness == 3:
                new_score = score * 0.5
            else:
                new_score = 0 

            adjusted_score += new_score
            assignment_count += 1

        if assignment_count > 0:
            student_average = adjusted_score / assignment_count
            average_scores.append(student_average)
        else:
            average_scores.append(0) 
            
    return average_scores

print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))




