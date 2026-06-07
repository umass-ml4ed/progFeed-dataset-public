# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def print_stars_to_file(n):
    with open (f'stars_{n}.txt', "w") as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i-1
            f.write (" " * spaces + "*" * stars + "\n")
        return None
    
print_stars_to_file(3)

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text=f.read()
        numbers = text.split('\n')
        numbers = [float(num) for num in numbers]
        average = (sum(numbers) / len(numbers))
    return average
    
print(calc_avg_from_file())

        