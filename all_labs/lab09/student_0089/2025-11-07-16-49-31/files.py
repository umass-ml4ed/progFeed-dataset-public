# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open('./stars_' + str(n) + '.txt', 'w') as s: #open the file
        counter = 1 #allows me to keep track of the spaces
        counterstars = 1 #allows me to get the correct number of stars
        while counter <= n: # stops when the counter is more than the input number
            s.write(" " * (n - counter) + ("*" * counterstars))
            s.write('\n') #creates a new line each time
            counter += 1
            counterstars += 2
# Call the function with n = 6
print_stars_to_file(3)

# Open the resulting file and print its contents
file_name = 'stars_3.txt'
with open(file_name, 'r') as f:
    contents = f.read()

print(contents)

def calc_avg_from_file():
    with open('./grades.txt', 'r') as f:
        text = f.read()
        grades_list = text.split('\n')
        total = 0
        count = 0
        for grade_string in grades_list:
            grade = float(grade_string)
            total += grade
            count += 1
        average = total / count
        return average