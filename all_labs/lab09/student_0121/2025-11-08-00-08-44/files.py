# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n): 
    file_name = f"stars_{n}.txt" #f string for different n values 
    with open(file_name, 'w') as f: 
        for i in range(1, n+1): 
            spaces = " " * (n-i) 
            stars = "*" * (2*i-1)
            f.write(spaces + stars + "\n")

def calc_avg_from_file():
    with open("grades.txt", "r") as f: 
        texts = f.read().strip() #removes empty lines
    grades = texts.split("\n")
    total = 0 
    for grade in grades: 
        total = total + float(grade)
    avg = total/len(grades)
    return avg 
