# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n: int):
    with open(f"stars_{n}.txt", "w") as f:
        for i in range(n):
            spaces = ' ' * (n - 1 - i)
            stars = '*' * (2 * i + 1)
            f.write(spaces + stars + "\n")
print_stars_to_file(5)         

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text= f.readlines()
        grades= []
        for i in text:
            grades.append(float(i.strip('\n')))
    avg = sum(grades)/ len(grades)
    return avg

        

