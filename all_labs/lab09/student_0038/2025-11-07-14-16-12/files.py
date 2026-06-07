# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open("stars_n.txt", "w") as file:
        file.write('*' * (n-1) + '*' + '\n')
        file.write('*'* (n-2) + "***" + '\n')
        file.write('*' * (n-3) + "*****" + '\n')
        file.write('*' * (n-4) + "*******" + '\n')
        for i in range(2, n + 1):
            file.write("*" * (2 * i - 1))
print_stars_to_file(3)