# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



# -----------------------------------------------------------
# 1. print_stars_to_file(n)
# -----------------------------------------------------------
def print_stars_to_file(n):
    """Creates a file 'stars_n.txt' containing n lines of centered stars."""
    filename = f"stars_{n}.txt"
    with open(filename, "w") as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = " " * spaces + "*" * stars
            print(line, file=f)  # print adds newline automatically


# -----------------------------------------------------------
# 2. calc_avg_from_file()
# -----------------------------------------------------------
def calc_avg_from_file():
    """Reads 'grades.txt' and returns the average of all grades."""
    with open("grades.txt", "r") as f:
        text = f.read().strip()  # remove any trailing newlines
        grades_list = text.split("\n")
        grades = [float(g) for g in grades_list]
        avg = sum(grades) / len(grades)
        return avg



