# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    stars_n=open('./stars_n.txt', 'w')
    for i in range(n): 
        stars_n.write(' '*(1+(n-i))+'*'*(1+i*2)+'\n')
    stars_n.close()

