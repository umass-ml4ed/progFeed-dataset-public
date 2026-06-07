# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "a") as file:
        stars = ""
        spaces = ""
        space_list = []
        star_list = []
        for value in range(1, n+1):
            spaces = " "*(n-value)
            space_list.append(spaces)
        for item in range(1, 2*n, 2):
            stars = "*"*(item)
            star_list.append(stars)
        for value in range(len(space_list)):
            line = space_list[value] + star_list[value] + "\n"
            file.write(line)

def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        text = file.read()
        text_list = text.split("\n")
        floated_text = [float(number) for number in text_list]
        average = sum(floated_text)/len(floated_text)
        return average

print(calc_avg_from_file())