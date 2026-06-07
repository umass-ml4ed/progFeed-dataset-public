# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    file = open("stars_{n}.txt","w")
    for i in range (1, n+1):
       spaces = " " * (n-i)
       stars = "*" * (2*i-1)
       line = spaces + stars + "\n"
       file.write(line)
    file.close()

print_stars_to_file(6)


def calc_avg_from_file():
    f = open("grades.txt","r")
    text = f.read()
    lst = text.split('\n')
    sum = 0 
    for i in lst:
        sum += float(i)
    avg = sum/(len(lst))
    
    f.close()