# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    fileName = f"stars_{n}.txt"
    with open(fileName, "w") as file:
        for i in range(1 , n+1):
            spaces = " " * (n - i)
            stars = '*' * ( 2 * i - 1)
            file.write(spaces + stars + "\n")

    print(f"File '{fileName}' created successfully.")
print_stars_to_file(3)

def calc_avg_from_file():
    with open("grades.txt", "r") as f: 
        text =f.read()
    tokens = [line.strip() for line in text.splitlines() if line.strip() != " "]
    grades = [float(i) for i in tokens]
    return sum(grades)/ len(grades)

