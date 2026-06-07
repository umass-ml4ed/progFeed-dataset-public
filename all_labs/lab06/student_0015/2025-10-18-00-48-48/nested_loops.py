# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED


# Function 1: get_names
# This function combines each first name with each last name
# using nested loops and returns a list of all possible full names.
def get_names(first_names, last_names):
    full_names = []
    for first in first_names:          # Outer loop: iterate over first names
        for last in last_names:        # Inner loop: iterate over last names
            full_name = first + " " + last
            full_names.append(full_name)
    return full_names


# Function 2: average_scores
# This function calculates the average grade for each student
# after applying lateness penalties, using nested loops.
def average_scores(scores):
    averages = []  # List to store each student's average

    for student in scores:  # Outer loop: each student
        total = 0
        count = 0

        for grade, late in student:  # Inner loop: each assignment
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

        average = total / count
        averages.append(average)

    return averages
