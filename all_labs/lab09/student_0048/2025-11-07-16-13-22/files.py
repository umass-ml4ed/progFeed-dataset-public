# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    stars_n=open(f'./stars_{n}.txt', 'w')
    for i in range(n): 
        stars_n.write(' '*(1+(n-i))+'*'*(1+i*2)+'\n')
    stars_n.close()
print_stars_to_file(6)

def calc_avg_from_file():
    grad=open('./grades.txt', 'r')
    text=grad.read()
    text.split('\n')
    lis=text.split('\n')
    num = 0
    tally = 0
    for i in lis:
        num+=1
        tally+=float(i)
    return(tally/num)

        


