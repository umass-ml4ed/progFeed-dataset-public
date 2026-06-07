# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            line = ' ' * (n - i) + '*' * (2 * i - 1)
            if i < n:
                f.write(line + '\n')
            else:
                f.write(line)
print_stars_to_file(4)


def calc_avg_from_file():
    grades = []
    with open('grades.txt', 'r') as f:
        for lineno, line in enumerate(f, start=1):
            s = line.strip()
            if not s:
                # skip empty lines
                continue
            try:
                grades.append(float(s))
            except ValueError:
                # helpful error message if the file has bad data
                raise ValueError(f"Invalid number on line {lineno}: {line!r}")
    if not grades:
        raise ValueError("grades.txt contains no valid grades.")
    return sum(grades) / len(grades)


print(calc_avg_from_file())

    