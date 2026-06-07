# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def print_stars_to_file(n):
    """
    Creates a file named stars_n.txt that contains n lines of stars.
    The first line has (n-1) spaces followed by 1 star.
    Each subsequent line decreases spaces by 1 and increases stars by 2.
    """
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = " " * spaces + "*" * stars
            print(line, file=f)


def calc_avg_from_file():
    """
    Reads grades from grades.txt and returns the average grade as a float.
    Assumes one grade per line with no trailing empty line.
    """
    with open("grades.txt", 'r') as f:
        text = f.read()
        grades_str = text.split('\n')
        grades = [float(g) for g in grades_str]
        average = sum(grades) / len(grades)
        return average
