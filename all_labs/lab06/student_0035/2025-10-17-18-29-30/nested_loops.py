# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names, last_names):
    names = [ ]
    for i in first_names:
        for j in last_names:
            names.append(i  + ' ' + j)
    
    return names

print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))


def average_scores(students):
    result = []
    
    for student in students:
        total = 0
        for grade, lateness in student:
            
            if lateness == 0:
                multiplier = 1
            elif lateness == 1:
                multiplier = 0.9
            elif lateness == 2:
                multiplier = 0.75
            elif lateness == 3:
                multiplier = 0.5
            else:
                multiplier = 0 
            
            total += grade * multiplier
        
        avg = total / len(student)
        result.append(avg)
    
    return result

students = [
  [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
  [(100, 10), (90, 0), (80, 0), (90, 0)],
  [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0)]
]

print(average_scores(students))
