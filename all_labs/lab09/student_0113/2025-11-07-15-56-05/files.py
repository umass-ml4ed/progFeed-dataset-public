#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f: 
        for i in range(1, n+1):
            line = ' ' * (n - i) + "*" * (2*i - 1)  
            print(line, file=f)

print_stars_to_file(6)

def calc_avg_from_file():
    filename = "grades.txt"
    with open(filename, "r") as f: 
        text = f.read()
        numbers = text.split("\n")
        count = 0 
        for number in numbers: 
            number = float(number)
            count += number 
        avg = count / len(numbers)
    return avg 

print(calc_avg_from_file())

