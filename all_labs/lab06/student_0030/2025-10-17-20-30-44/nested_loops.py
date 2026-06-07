def get_names(first_names, last_names):

    full_names = []
    for first in first_names:
        for last in last_names:
            full_names = first + " " + last
            full_names.append(full_names)
    return full_names
        
def average_scores(all_students):
    averages = []
    for student in all_students:
        total = 0
        count = 0
        for grade, late_credit in student:
            if late_credit == 0:
                penalty = 1.0
            if late_credit == 1:
                penalty = 0.9
            if late_credit == 2:
                penalty = 0.75
            if late_credit == 3:
                penalty = 0.5
            else:
                penalty = 0
            total += grade * penalty
            count += 1
        average = total/count
        averages.append(average)
    
    