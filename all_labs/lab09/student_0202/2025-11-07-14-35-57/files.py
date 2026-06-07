# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    stars = open(f"stars_{n}.txt","a")
    for i in range(1,n+1):
        stars.write((n-i)*" " + (2*i-1) * "*"+"\n")

def calc_avg_from_file():
    grades = open("grades.txt","r")
    text = grades.read()
    grades_list = text.split("\n")
    grade_float = []
    for i in grades_list:
        try:
            grade_float.append(float(i))
        except:
            continue
    for i in grade_float:
        total_grade += i
    average_grade = total_grade/grade_float.len()
    return average_grade

print_stars_to_file(4)