# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    filename = "stars_" + str(n) + ".txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            line = spaces + stars
            print(line, file=f) 

print_stars_to_file(3)


def calc_avg_from_file():
    file = open("grades.txt", "r")
    text = file.read()
    file.close()

    grades_str = text.split('\n')
    grades_float = []
    for g in grades_str:
        grades_float.append(float(g))
    total = 0
    for num in grades_float:
        total = total + num
        
    average = total / len(grades_float)

    return average

print(calc_avg_from_file())