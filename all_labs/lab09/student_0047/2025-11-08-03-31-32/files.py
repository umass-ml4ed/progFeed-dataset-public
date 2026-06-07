# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file=f'stars_{n}.txt'
    with open(file,'w') as f:
        for num in range(1,n+1):
            print(" "*(n-num)+"*"*(2*num-1),file=f)
        
def calc_avg_from_file():
    file='grades.txt'
    with open(file,'r') as f:
        content=f.read()
    content=content.split('\n')
    total=0
    for num in content:
        total+=float(num)
    return total/len(content)


    