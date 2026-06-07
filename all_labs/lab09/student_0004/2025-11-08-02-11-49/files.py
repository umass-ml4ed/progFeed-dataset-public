# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n: int):
    filename = f"stars_{n}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = (" " * spaces) + ("*" * stars)
            f.write(line + "\n")


def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        nums = [float(x) for x in f.read().split("\n")]
    return sum(nums) / len(nums)
