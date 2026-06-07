# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", "w")
    for num in range(1,n + 1):
        print((" " * (n-num)) + ("*" * (2 * num - 1)), file = f)
    f.close()
print_stars_to_file(6)
