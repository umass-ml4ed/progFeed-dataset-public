# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    
    with open(filename, 'w') as file:

        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)

            line = spaces + stars
            print(line, file=file)

def calc_avg_from_file():
    try:
        with open('grades.txt', 'x') as file:
            file.write("82.5\n93\n77.5\n65")
        print("Created grades.txt with sample data")
    except FileExistsError:
        print("grades.txt already exists, using existing file")
    
    with open('grades.txt', 'r') as file:
        content = file.read().strip()
    
    print(f"File content: '{content}'")
    
    lines = content.split('\n')
    grades = []
    
    for line in lines:
        line = line.strip()
        if line: 
            try:
                grades.append(float(line))
            except ValueError:
                print(f"Warning: Could not convert '{line}' to float")
    
    print(f"Grades found: {grades}")
    
    if grades:
        average = sum(grades) / len(grades)
        return average
    else:
        return 0.0


result = calc_avg_from_file()
print(f"Average: {result}")

result2 = print_stars_to_file(10)
print(f"Average: {result2}")
