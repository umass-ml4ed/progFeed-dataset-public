def print_stars_to_file(n):
    """Print a centered star pattern of height n to a file."""
    fname = 'stars_'+str(n)+'.txt'
    with open(fname, 'w') as f:
        for i in range(1, n + 1):
            line = ' ' * (n - i) + '*' * (2 * i - 1) + '\n'
            f.write(line)

def calc_avg_from_file(fname='grades.txt'):
    """Calculate the average of grades stored in a file."""
    with open(fname, 'r') as f:
        grades = [float(line.strip()) for line in f if line.strip()]
    if not grades:
        return 0.0
    return sum(grades) / len(grades)