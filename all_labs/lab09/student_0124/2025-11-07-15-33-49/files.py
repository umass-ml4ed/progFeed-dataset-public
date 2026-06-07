# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# create function for making and writing into a file
def print_stars_to_file(n:int):
    stars = list(range(1,2*n, 2))
    with open(f"stars_{n}.txt", "w") as file:
        for line in range(1, n+1):
            file.write(f"{(n-line) * ' '}{stars[line-1]*'*'}\n")
            

def calc_avg_from_file() -> float:
    with open("grades.txt", 'r') as file:
        text = file.read()
        text = text.strip().split('\n')
        for stuff in text:
            stuff = stuff.strip()
        tot = 0
        num = len(text)
        for nums in text:
            tot += int(nums)
        avg = tot/num
        
