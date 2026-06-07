# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open (f'stars_{n}.txt', 'w') as file:
        for x in range(1, n+1):
            file.write(' ' *(n-x))
            file.write('*' *((2*x)-1))
            file.write('\n')

def calc_avg_from_file():
    with open ('grades.txt', 'r') as f:
        text = f.read()
        lst=text.split('\n')
        total=0
        for x in lst:
            total+=float(x)
        average= total/len(lst)
        return average 
