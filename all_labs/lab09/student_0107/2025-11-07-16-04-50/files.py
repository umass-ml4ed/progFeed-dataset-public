# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    stars = open(f'stars_{n}.txt', 'w') 
    for i in range(n): 
        stars.writelines((' '*(n-i)))
        stars.writelines("*"* (2*(i) + 1) + '\n')
        


def calc_avg_from_file():
    file = open(f"grades.txt", 'r')
    numbers = file.read().split("\n")
    ans = 0
    for i in range(len(numbers)):
        ans = ans + float(numbers[i])
    ans = ans/len(numbers)
    

