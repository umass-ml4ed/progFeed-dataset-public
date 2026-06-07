# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

"""
takes two lists of strings: one representing a list of first names (given names), 
the other a list of last names (surnames), and the function returns a new list 
that contains all combinations of first names and last names.
"""
def get_names(first_names,last_names):
    full_names = []
    for give_name in first_names:
        for surnames in last_names:
            full_name = give_name + " " + surnames
            full_names.append(full_name)
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']


"""
calculates the average grade for each student after applying a lateness penalty. 
The input is a list of lists, where each inner list represents a student's assignments. 
Each assignment is represented as a tuple of (grade, lateness). Grades are between 0 and 100 inclusive.
"""
def average_scores(scores):
    averages = []

    for student in scores:
        total = 0
        count = 0
        for assignment in student: 
            grade = assignment[0]
            lateness = assignment[1]            
            if lateness == 0:
                credit = 1.0
            elif lateness == 1:
                credit = 0.9
            elif lateness == 2:
                credit = 0.75
            elif lateness == 3:
                credit = 0.5
            else:
                credit = 0.0

            adjusted_grade = grade * credit
            total += adjusted_grade
            count += 1

        average = total / count
        averages.append(average)
    return averages 

scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
