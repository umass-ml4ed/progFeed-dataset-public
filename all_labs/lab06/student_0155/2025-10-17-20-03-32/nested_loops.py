# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(i + " " + j)
    return full_names

#first_names = ['Ari', 'Taylor']
#last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
#print(get_names(first_names, last_names)) # ['Ari Levine', 'Ari Lopez', 'Ari Khan', 'Ari Wang', 'Taylor Levine','Taylor Lopez', 'Taylor Khan', 'Taylor Wang']

def average_scores(students):
    final_scores = []
    for student in students:
        total = 0
        for scores in student:
            match scores[1]:
                case 0:
                    mod = 1
                case 1:
                    mod = 0.9
                case 2:
                    mod = 0.75
                case 3:
                    mod = 0.5
                case _:
                    mod = 0
            total += scores[0] * mod
            final = total / len(student)
        final_scores.append(final)
    return final_scores

#scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
#          [(100, 10), (90, 0), (80, 0), (90, 0)], 
#          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

#print(average_scores(scores)) # [48.9, 65.0, 59.333333333333336]