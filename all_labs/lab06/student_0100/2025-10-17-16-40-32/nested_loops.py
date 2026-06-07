# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names:list, last_names:list):
    full_names = []
    for f_names in first_names:
        for l_names in last_names:
            full = f"{f_names} {l_names}"
            full_names.append(full)
    return full_names

print(get_names(['Ari', 'Taylor'],['Levine', 'Lopez', 'Khan', 'Wang']))

def average_scores(scores:list):
    cummulative_average = []
    for results in scores:
        total_grade = 0
        for student in results:
            grade = student[0]
            lateness = student[1]
            if lateness == 0:
                final_grade = grade
            elif lateness == 1:
                final_grade = grade * 0.9
            elif lateness == 2:
                final_grade = grade * 0.75
            elif lateness == 3:
                final_grade = grade * 0.5
            elif lateness >= 4:
                final_grade = grade * 0
            total_grade += final_grade
        average = total_grade/len(results)
        cummulative_average.append(average)


    return cummulative_average
    
print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
              [(100, 10), (90, 0), (80, 0), (90, 0)], 
              [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))