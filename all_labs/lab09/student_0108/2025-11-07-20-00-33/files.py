# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", 'w') as file:
        for i in range(1, n+1):
            print((' '*(n-i))+('*'* (2*i -1)), file=file)


def calc_avg_from_file():
    sum=0
    with open("grades.txt", 'r') as f:
        text=f.read()
        text.split('\n')
        for grade in text:
            sum+=float(grade)
    avg=sum/len(text)
    return avg

print(calc_avg_from_file())