# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f= "stars_" + str(n) + ".txt"
    file= open(f, "w")

    for i in range(1,n +1):
        space= n-i
        star= 2*i - 1
        line= " " *space + "*" *star
        file.write(line + "\n")

    f.close()

def calc_avg_from_file():
  
    f= open("C:/Users/ajcog/CICS 110/Labs/Lab 9/grades.txt", "r")
    text= f.read()
    f.close()
    grades= text.split("\n")
    total = 0
    count= 0

    for grade in grades:
        total = total + float(grade)
        count= count + 1

    avg= total / count

    return avg