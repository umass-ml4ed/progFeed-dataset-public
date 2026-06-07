# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open('stars_n.txt','w') as f:
        for i in range(1,n+1):
            spaces=n-i
            star=2*i-1
            print(' '*spaces+'*'*star,file=f)

def calc_avg_from_file():
    with open('print_stars_to_file(n)','w') as f:
        text=f.read()
    grade_strings=[s for s in text.split('/n') if s.strip()]
    grade=[float(s) for s in grade_strings]
    return sum(grade)/len(grade)