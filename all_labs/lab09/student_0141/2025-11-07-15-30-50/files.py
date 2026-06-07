# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, "w") as f:
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            stars = "*" * (2 * i - 1)
            f.write(spaces + stars + "\n")


def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read().strip()  # Remove any extra newlines or spaces
        grades = text.split("\n")
        grades = [float(g) for g in grades if g.strip() != ""]  # Convert to floats and skip blanks
        if len(grades) == 0:
            return 0.0
        return sum(grades) / len(grades)

