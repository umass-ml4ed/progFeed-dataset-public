# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'./stars_{n}.txt','w') as file:
        for line in range(1,n):
            file.write(" " * (n - line) + '*' * (line + (line - 1)) + "\n")
        file.write('*' * (2 * n - 1))

print_stars_to_file(6)

def calc_avg_from_file():
    with open('./grades.txt','r') as file:
        text = file.read()
        new_text = text.split('\n')
        total = 0
        for score in new_text:
            total += float(score)
    return total / len(new_text)

#print(calc_avg_from_file())