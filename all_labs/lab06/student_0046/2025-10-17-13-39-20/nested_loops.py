# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    """
    Takes two lists of strings (first and last names) and returns
    a list of all possible full name combinations.
    """
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names


def average_scores(scores):
    """
    Takes a list of lists of (grade, lateness) tuples and returns
    the average adjusted grade for each student.
    """
    result = []
    for student in scores:
        total = 0
        for grade, late in student:
            if late == 0:
                penalty = 1.0
            elif late == 1:
                penalty = 0.9
            elif late == 2:
                penalty = 0.75
            elif late == 3:
                penalty = 0.5
            else:
                penalty = 0.0
            total += grade * penalty
        avg = total / len(student)
        result.append(avg)
    return result

if __name__ == "__main__":
    first_names = ['Ari', 'Taylor']
    last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
    print(get_names(first_names, last_names))
    # ['Ari Levine', 'Ari Lopez', 'Ari Khan', 'Ari Wang', 'Taylor Levine', 'Taylor Lopez', 'Taylor Khan', 'Taylor Wang']

    scores = [
        [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
        [(100, 10), (90, 0), (80, 0), (90, 0)],
        [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
    ]
    print(average_scores(scores))
    # Output: [48.9, 65.0, 59.333333333333336]
