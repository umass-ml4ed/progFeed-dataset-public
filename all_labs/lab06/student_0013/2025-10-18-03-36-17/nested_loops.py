# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names, last_names):
    combos = []
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            combos.append(first_names[i] + " " + last_names[j])
    return combos


firsts = ['Ari', 'Taylor']
lasts = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(firsts, lasts))

def average_scores(scores):
    result = []

    for student in scores:
        total = 0
        for grade, late in student:
            if late == 0:
                total += grade * 1
            elif late == 1:
                total += grade * 0.9
            elif late == 2:
                total += grade * 0.75
            elif late == 3:
                total += grade * 0.5
            else:
                total += 0
        average = total / len(student)
        result.append(average)
    
    return result


scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
]

print(average_scores(scores))
