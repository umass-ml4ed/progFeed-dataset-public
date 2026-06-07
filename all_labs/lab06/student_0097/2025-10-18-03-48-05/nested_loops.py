# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
#Function must return 8 names (fxj)
def get_names(string1,string2):
    full_names = []
    for i in string1:
        for j in string2:
            x = f'{i} {j}'
            full_names.append(x)
    return full_names

print(get_names(first_names,last_names))


The_grades = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
def average_scores(grades):
    averages = []
    penalties = {0:1.00, 1:0.90, 2:0.75, 3:0.50}
    for student in grades:
        total = 0
        count = 0

        for grade, late in student:
            multiplier = penalties.get(late, 0)
            total += grade * multiplier
            count += 1

        averages.append(total/count)
    return averages

    

#working with tuples
print(average_scores(The_grades))

#Output → [48.9, 65.0, 59.333333333333336]

#For the first student: (90 + 80 * 0.9 + 70 * 0.75 + 60 * 0.5 + 50 * 0) / 5 = 48.9
#or the second student: (100 * 0 + 90 + 80 + 90) / 4 = 65.0
#For the third student: (0 + 20 + 40 * 0.9 + 100 + 100 + 100) / 6 = 59.3333
