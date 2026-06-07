#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def print_stars_to_file(n: int):
    with open(f'stars_{n}.txt', 'w') as f:
        numbers = range(1, n)
        count1 = 1
        count2 = 1
        for number in numbers:
            print(f'{" "*(n-count1) + "*"*count2}', file=f)
            count1 += 1
            count2 += 2
        print(f'{"*"*(2*n-1)}', file=f, end='')

def calc_avg_from_file() -> float:
    with open('grades.txt', 'r') as f:
        text = f.read()
        numbers = text.split('\n')
        total = 0
        for n in numbers:
            total += float(n)
        return total/len(numbers)
        


        


