# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#1
def print_stars_to_file(n: int) -> None:
    """
    Create a file named "stars_n.txt" and write n lines forming a centered
    triangle of stars. Assumes n >= 1.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    filename = f"stars_{n}.txt"
    with open(filename, "w") as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = " " * spaces + "*" * stars
            f.write(line + "\n")

#2
def calc_avg_from_file() -> float:
    with open("grades.txt", "r") as f:
        text = f.read()
    
    
    grades_str = text.split('\n')
    
   
    grades = [float(g) for g in grades_str]
    
    avg = sum(grades) / len(grades)
    return avg
