# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
if __name__ == "__main__":
    first_names = ['Ari', 'Taylor']
    last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
def get_names():
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names
def average_scores(all_scores):
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}
    averages = []
    for student in all_scores:
        total = 0
        for grade, late in student:
            if late >= 4:
                factor = 0
            else:
                factor = penalties[late]
            total += grade * factor
        averages.append(total / len(student))
    return averages