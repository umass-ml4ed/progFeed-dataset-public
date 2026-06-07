# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names,last_names):
    full_names = []
    for i in range(len(first_names)):
        full = first_names[i] + " " + last_names[i]
        full_names.append(full)
    return full_names

def average_scores(parameter):
    after = []
    for student_scores in parameter:
        student_adjusted_scores = []
        for item in student_scores:
            grade = item[0]
            lateness = item[1]
  
            if lateness == 0:
                grade1 = grade
                student_adjusted_scores.append(grade1)
            elif lateness == 1:
                grade2 = grade * 0.9
                student_adjusted_scores.append(grade2)
            elif lateness == 2:
                grade3 = grade * 0.75
                student_adjusted_scores.append(grade3)
            elif lateness == 3:
                grade4 = grade * 0.5
                student_adjusted_scores.append(grade4)
            else:
                grade5 = grade * 0
                student_adjusted_scores.append(grade5)
        average = sum(student_adjusted_scores) / len(student_adjusted_scores)
        after.append(average)
            
    return after
                
