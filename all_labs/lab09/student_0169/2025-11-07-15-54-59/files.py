def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars, file=f)

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read().strip()  
        grades = text.split('\n')  
        numbers = [float(g) for g in grades]  
        avg = sum(numbers) / len(numbers)
        return avg
