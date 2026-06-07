# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']


def get_names(first, last):
    result = []
    for f in first:
        for l in last:
            result.append(f + " " + l)
    return result



scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def average_scores(students):
    results = []
    for students in students:
        total = 0
        for grade, late in students:
            if late == 0:
                penalty = 1
            elif late == 1:
                penalty = 0.9
            elif late == 2:
                penalty = 0.75
            elif late == 3:
                penalty = 0.5
            else:
                penalty = 0
            total += grade * penalty
        average = total / len(students)
        results.append(average)
    return results


print(average_scores(scores))

