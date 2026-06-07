# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    """
    Takes two lists: first_names and last_names.
    Returns a list containing all combinations of first and last names.
    """
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names


def average_scores(students):
    """
    Takes a list of lists of tuples in the form (grade, lateness)
    and returns a list of average grades after applying lateness penalties.
    """
    averages = []

    for student in students:
        total = 0
        count = 0
        for grade, late in student:
            if late == 0:
                multiplier = 1.0
            elif late == 1:
                multiplier = 0.9
            elif late == 2:
                multiplier = 0.75
            elif late == 3:
                multiplier = 0.5
            else:
                multiplier = 0.0

            total += grade * multiplier
            count += 1

        avg = total / count if count > 0 else 0
        averages.append(avg)

    return averages


# Example tests (you can remove or comment these out before submission)
if __name__ == "__main__":
    first_names = ['Ari', 'Taylor']
    last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
    print(get_names(first_names, last_names))
    
    scores = [
        [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
        [(100, 10), (90, 0), (80, 0), (90, 0)],
        [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
    ]
    print(average_scores(scores))
