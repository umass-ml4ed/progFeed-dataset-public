# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n: int) -> None:

    filename = f"stars_{n}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars, file=f)  

def calc_avg_from_file() -> float:
    
    with open("grades.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines() 
    grades = [float(x) for x in lines if x != ""]
   
    return sum(grades) / len(grades)
