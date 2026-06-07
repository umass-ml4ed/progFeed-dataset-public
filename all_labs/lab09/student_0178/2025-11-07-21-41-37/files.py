# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def print_stars_to_file(n):
    fh=open(f"stars_{n}.txt",'w')
    for j in range(0,n):
        for i in range(n,j+1,-1):
            fh.write(' ')
        fh.write('*'*(((j+1)*2)-1))
        fh.write('\n')


def calc_avg_from_file():
    fh=open('grades.txt','r')
    s=fh.read()
    l=s.split('\n')
    total=0
    length=len(l)
    for i in l:
        total+=float(i)
    avg=total/length
    return avg
