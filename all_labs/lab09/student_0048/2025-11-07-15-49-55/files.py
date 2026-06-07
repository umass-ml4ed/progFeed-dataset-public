# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    stars_n=open('./stars_n.txt', 'w')
    for i in range(n+1): 
        stars_n.write(' '*(1+(n-i))+'*'*(1+(i-1)*2)+'\n')
    stars_n.close()
print_stars_to_file(3)
