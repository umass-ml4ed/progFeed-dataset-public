# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def print_stars_to_file(n):
    fname = f"stars_{n}.txt"
    with open(fname, "w") as f:
        for i in range(1, n+1):
            leading_space = n - i
            num_star = 2*i-1
            line = ' ' * leading_space + '*' * num_star
            print(line, file=f)
print_stars_to_file(3)


def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read
        grade_str = text.split('\n')
    grades = [float(grade) for grade in grade_str]
    avg_grades = sum(grades)/len(grades)
    return avg_grades
#print(calc_avg_from_file())
