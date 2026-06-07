# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def print_stars_to_file(n: int):
    with open(f'stars_{n}.txt', 'w') as file:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            file.write(spaces + stars + '\n')
    return

print_stars_to_file(4)

def calc_avg_from_file():
    with open('grades.txt','r') as file:
        contents=file.read()
        grades=list(contents.split('\n'))

        converted_grades=[]
        for item in grades:
            value=float(item)
            converted_grades.append(value)

        total=sum(converted_grades)

        average=total/len(converted_grades)
        return average






