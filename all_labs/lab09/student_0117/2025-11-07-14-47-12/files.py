# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as s:
        for x in range(n):
            count_from_zero = x+1
            s.write(((((n - count_from_zero)*" ") + ((2*count_from_zero-1)*"*"))+"\n"))

def calc_avg_from_file():
    with open(f'grades.txt', "r") as g:
        text = g.read()
        whole_list = text.split("\n")
        sum = 0
        count = 0
        for grade in whole_list:
            sum += float(grade)
            count += 1
        return sum/count
