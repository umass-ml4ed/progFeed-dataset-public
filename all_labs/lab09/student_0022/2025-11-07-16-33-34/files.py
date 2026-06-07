# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "a") as file:
        for value in range(1, n+1):
            spaces = " "*(n-value)
            stars = "*"*(2*value - 1)
            if value == n:
                file.write(spaces+stars+"\n")
            else:
                file.write(spaces+stars)

def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        text = file.read()
        text_list = text.split("\n")
        floated_text = [float(number) for number in text_list]
        return sum(floated_text)/len(floated_text) if floated_text else 0
