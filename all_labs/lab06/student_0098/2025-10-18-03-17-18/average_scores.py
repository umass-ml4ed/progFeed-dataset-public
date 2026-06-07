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
        list: A list where each element is the average grade of each student after applying penalties.
    """
    def apply_penalty(grade, lateness):
        """
        Applies the lateness penalty to the given grade.

        Args:
            grade (int): The raw grade of the assignment.
            lateness (int): The lateness of the assignment.

        Returns:
            float: The grade after applying the lateness penalty.
        """
        if lateness == 0:
            return grade
        elif lateness == 1:
            return grade * 0.9
        elif lateness == 2:
            return grade * 0.75
        elif lateness == 3:
            return grade * 0.5
        else:
            return 0

    student_averages = []
    for student_scores in scores:
        total_score = 0
        for grade, lateness in student_scores:
            total_score += apply_penalty(grade, lateness)
        student_averages.append(total_score / len(student_scores))

    return student_averages        
