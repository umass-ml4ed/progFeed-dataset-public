# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED



def print_stars_to_file(n: int) -> None:
   
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for k in range(1, n + 1):
            spaces = n - k
            stars = 2 * k - 1
            line = ' ' * spaces + '*' * stars
            f.write(line + '\n')





def calc_avg_from_file() -> float:
   
    with open('grades.txt', 'r') as f:
        text = f.read().strip()   

    grades_str = text.split('\n') 
    grades = [float(g) for g in grades_str]

    avg = sum(grades) / len(grades)
    return avg
