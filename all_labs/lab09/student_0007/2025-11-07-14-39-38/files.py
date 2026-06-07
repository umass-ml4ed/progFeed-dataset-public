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
        if i != n:
            file.write(line + "\n")
        else:
            file.write(line)

    file.close()



def calc_avg_from_file():
  
    with open("grades.txt", "r") as f:
        text = f.read()
    f.close()
    grades= text.split("\n")
    total = 0
    count= 0

    for grade in grades:
        total = total + float(grade)
        count= count + 1

    avg= total / count

    return avg