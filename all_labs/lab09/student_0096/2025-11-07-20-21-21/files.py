# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file=open(f'./stars_{n}.txt','w')
    for i in range(1,n+1):
        spaces=n-i
        stars=2*i-1
        line=' '*spaces+"*"*stars
        file.write(line)
        if i !=n:
            file.write('\n')


def calc_avg_from_file():
    with open('./grades.txt','r') as f:
        text=f.read()
        text.split('\n')
        return sum(text)/len(text)
        

