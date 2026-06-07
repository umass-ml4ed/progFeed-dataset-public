# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as file:
        for i in range(n):
            file.write(f"{(n - i) * ' '}{'*' * (2 * i - 1)}\n")
        
        

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        new_text = text.split('\n')
        total = 0 
        # print(new_text)
        for c in new_text:
            total += float(c)
        return total / len(new_text)

