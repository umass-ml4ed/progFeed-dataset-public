#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt','w') as file:
        for i in range(n):
            file.write((n-(i+1))*' ' + (2*i+1)*'*' + '\n')

def calc_avg_from_file():
    with open('grades.txt','r') as file:
        text = file.read()
        lst = text.split('\n')
        sum = 0
        for grade in lst:
            sum += float(grade)
        return sum/len(lst)
