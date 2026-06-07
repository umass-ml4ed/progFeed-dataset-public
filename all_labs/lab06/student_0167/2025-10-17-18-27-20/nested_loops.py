# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_names = []
    for i in range(0,len(first_names)):
        for j in range(0,len(last_names)):
            full_names.append(first_names[i] + " " + last_names[j])
    return full_names


def average_scores(student_assignments):
    averages = []
    
    for student in range(0, len(student_assignments)):
        total_penalized_grade = 0
        
        for set_of_marks in range(0, len(student_assignments[student])):
            raw_grade = student_assignments[student][set_of_marks][0]
            lateness = student_assignments[student][set_of_marks][1]

            if lateness == 0:
                credit = 1.0
            elif lateness == 1:
                credit = 0.9
            elif lateness == 2:
                credit = 0.75
            elif lateness == 3:
                credit = 0.5
            else:  # lateness >= 4
                credit = 0.0
            
            penalized_grade = raw_grade * credit
            total_penalized_grade += penalized_grade
        
        # Calculate average for this student
        average = total_penalized_grade / len(student_assignments[student])
        averages.append(average)
    
    return averages



