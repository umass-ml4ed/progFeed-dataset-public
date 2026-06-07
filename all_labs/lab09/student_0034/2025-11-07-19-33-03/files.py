# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", 'w') as f:
        it = n-1
        for num in range(1, n+1):
            f.write(" "*it+'*'*(2*num-1)+" "*it+'\n')
            it -= 1
    return

print_stars_to_file(3)

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        lines = f.readlines()
        nums = []
        for num in lines:
            nums.append(float(num.strip()))
        avg = sum(nums) / len(nums)
    return avg

#print(calc_avg_from_file())