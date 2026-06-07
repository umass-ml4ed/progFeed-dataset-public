# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n : int):
    with open(f"stars_{n}.txt", 'w') as f:
        for i in range(1,n+1):
            spaces = " " * (n-i)
            star = "*" * (2*i-1)
            f.write(f'{spaces}{star}\n')        

def calc_avg_from_file():
    with open(f'grades.txt', 'r') as f:
        text = f.read()
        lst = text.split("\n")
    total = 0 
    count = 0
    for i in lst:
        if i != '':
            total += float(i)
            count +=1
    return total / count




    

    
