# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

""" 
It should take an integer n as a parameter (you can assume n>=1), and it should create a text file named stars_n.txt,
where n is the actual value of the parameter n.
 """
def print_stars_to_file(n):
    filename = "stars_" + str(n) + ".txt"
    f = open(filename, "w")

    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        f.write(spaces + stars + "\n")
    f.close()  

"""
It takes no parameters, and its task is to calculate and return the average grade from a text file named grades.txt, 
which stores the students’ grades, one number per line
"""
def calc_avg_from_file():
    f = open("grades.txt", "r")
    text = f.read()  
    f.close()

    grade_strings = text.split("\n")
    total = 0
    count = 0

    for g in grade_strings:
        total = total + float(g)
        count = count + 1

    average = total / count
    return average

