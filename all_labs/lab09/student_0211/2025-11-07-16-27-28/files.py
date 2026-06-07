# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n : int):
    with open(f"stars_{n}.txt", 'w') as f:
        for i in range(1,n+1):
            spaces = " " * (n-i)
            star = "*" * (2*i-1)
            f.write(f'{spaces}{star}\n')
            


print(print_stars_to_file(5))

def calc_avg_from_file():
    f = open("grades.txt", 'r')
    text = f.read()
    lst = text.split("\n")
    sum = 0 
    for i in lst:
        sum += float(i)
    return sum / len(lst)

print(calc_avg_from_file())


    

    
