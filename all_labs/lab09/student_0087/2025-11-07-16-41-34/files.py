# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file = f"stars_{n}.txt"
    with open(file, 'w') as f:
        for i in range(1, n + 1):  
            spaces = ' ' * (n - i)          
            stars = '*' * (2 * i - 1)  
            line = spaces + stars           
            print(line, file=f)
def calc_avg_from_file ():
    with open ('grades.txt', 'r') as f:
        text = f.read ()
        text.split('\n')
        count = 0
        sum = 0
        for i in text:
            float (i)
            sum += i
            count +=1
            return sum/count
