# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open (f'stars_{n}.txt' , 'w') as f:
        for i in range(1,n):
            f.write(' '*(n-i)+'*'*(2*i-1)+'\n')
        f.write('*'*(2*n-1))


def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        content = text.split('/n')
        content = [float(x) for x in text.split('\n') if x.strip() !=0 ]
        return sum(content)/len(content)    





