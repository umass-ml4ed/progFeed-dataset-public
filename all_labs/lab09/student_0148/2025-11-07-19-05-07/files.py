 # Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = "stars_" + str(n) + ".txt"
    with open(filename, "w") as file:
        for x in range(1, n + 1):
            spaces = n - x
            stars = 2 * x - 1
            file.write(" " * spaces + "*" * stars + "\n")
    return filename

def calc_avg_from_file():
    sum_ = 0.0
    count = 0
    with open("grades.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                value = float(line)
            except ValueError:
                continue
            sum_ += value
            count += 1
    if count == 0:
        return 0.0
    return sum_ / count

if __name__ == "__main__":
    print(print_stars_to_file(3))
    print(calc_avg_from_file())
