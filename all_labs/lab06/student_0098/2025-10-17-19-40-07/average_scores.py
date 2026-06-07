# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def average_scores(scores):
    """
    Calculates the average grade for each student after applying a lateness penalty.

    Args:
        scores (list): A list of lists, where each inner list represents a student's assignments.
                      Each assignment is represented as a tuple of (grade, lateness).

    Returns:
        list: A list of average grades for each student after applying the lateness penalty.
    """
    student_averages = []

    for student_scores in scores:
        total_score = 0
        total_assignments = 0

        for grade, lateness in student_scores:
            if lateness == 0:
                penalty = 1.0
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            else:
                penalty = 0.0

            total_score += grade * penalty
            total_assignments += 1

        student_average = total_score / total_assignments
        student_averages.append(student_average)

    return student_averages
