# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n:int):
    filename = f"stars_{n}.txt"
    with open(filename, "w") as f:
        for i in range(n):
            spaces = " " * (n - 1 - i)
            stars = "*" * (2 * i + 1)
            f.write(spaces + stars + "\n")

# if __name__ == "__main__":
#     print_stars_to_file(8)

def calc_avg_from_file() -> float:
    with open("grades.txt", "r") as f:
        text = f.read()
    
    grades_str = text.split('\n')
    grades_actual = []
    for g in grades_str:
        grades_actual.append(float(g))
    avg = sum(grades_actual) / len(grades_actual)

    return avg

if __name__ == "__main__":
    print(calc_avg_from_file())
