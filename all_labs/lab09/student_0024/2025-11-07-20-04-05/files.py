def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        for i in range(n):
            spaces = ' ' * (n - i - 1)
            stars = '*' * (2 * i + 1)        # Use 'i' here
            f.write(spaces + stars + "\n")

        
def calc_avg_from_file():
    with open("grades.txt", "r") as f:       # Open the file for reading
        text = f.read()                      # Read full text
        grades = text.split('\n')            # Split on newlines
        nums = [float(g) for g in grades if g != ""]  # Convert each non-empty string to float
        avg = sum(nums) / len(nums)
        return avg
