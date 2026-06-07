# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):    
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(n):
            spaces = ' ' * (n - i - 1)
            stars = '*' * (2 * i + 1)
            line = spaces + stars
            print(line, file=f)

def calc_avg_from_file():
    try:
        with open('grades.txt', 'r') as f:
            text = f.read()
        grades_str = text.split('\n')
        grades_str = [grade for grade in grades_str if grade.strip() != '']
        grades = [float(grade) for grade in grades_str]
        if len(grades) > 0:
            return sum(grades) / len(grades)
        else:
            return 0.0
            
    except FileNotFoundError:
        print("Error: grades.txt file not found")
        return 0.0
    except ValueError:
        print("Error: Invalid data in grades.txt")
        return 0.0

if __name__ == "__main__":
    print_stars_to_file(3)
    print_stars_to_file(6)
    try:
        average = calc_avg_from_file()
        print(f"Average grade: {average}")
    except:
        print("Could not calculate average - make sure grades.txt exists")