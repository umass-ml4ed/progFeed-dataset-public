def print_stars_to_file(n):
    with open (f"stars_{n}.txt", "w") as f:
        for i in range(n):
            spaces = ' ' * (n - i - 1)
            stars = '*' * (2 * 1 + 1)
            f.write(spaces + stars + "\n")
        
def calc_avg_from_file():
    grades.txt = str
    text = f.read()
    grades = text.split('\n')
    nums = [float(g) for g in grades if g != ""]
    avg = sum(nums) / len(nums)
    return avg