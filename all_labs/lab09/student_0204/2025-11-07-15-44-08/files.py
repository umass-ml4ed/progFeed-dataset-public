# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):

    with open(f"stars_{n}.txt", "w") as newFile:
        starMult = 1
        for i in range(n):
            mult = n-i-1
            newFile.write(mult*" "+starMult*"*"+"\n")
            starMult += 2


def calc_avg_from_file():
    with open("grades.txt", "r") as gradesFile:
        grades = gradesFile.readlines()
        sum = 0
        for eachGrade in grades:
            try:
                sum += float(eachGrade.strip("\n"))
            except ValueError:
                print("error")
                continue
        return sum/len(grades)