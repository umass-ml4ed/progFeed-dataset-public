# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open('stars_'+str(n)+'.txt', 'w') as file:
        for i in range(1, 1+n):
            file.write(" "*(n-i)+ '*'*(2*i-1)+"\n")
    

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        grade_list = text.split('\n')
        total = 0
        for grade in grade_list:
            grade = float(grade)
            total += grade
        return(total/len(grade_list))
        
print_stars_to_file(6)
print_stars_to_file(3)
