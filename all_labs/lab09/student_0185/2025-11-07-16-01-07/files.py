# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n: int):
    with open(f"stars_{n}.txt", "w") as f:
        for stars in range(1, n+1):
            f.write(f"{' '*(n-stars)}{'*'*((stars*2)-1)}\n")

# print_stars_to_file(3)

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        grade = f.readlines()
        count = 0
        for num in grade:
            count += float(num)
        return count/len(grade)
    
# print(calc_avg_from_file())