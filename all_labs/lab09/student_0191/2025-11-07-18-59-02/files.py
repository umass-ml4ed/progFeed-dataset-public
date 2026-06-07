def print_stars_to_file(n):
    with open(f"Lab 9/stars_{n}.py", "w") as f:
        count = 1
        for i in range(1, n+1):
            f.write(((n-count) * " ") + ((2*(i) - 1) * "*") + "\n")
            count += 1

def calc_avg_from_file():
    with open("./Lab 9/grades.txt", "r") as f:
        string = f.read()
        grades = string.split("\n")
        for i in range(len(grades)):
            grades[i] = float(grades[i])

        return sum(grades)/len(grades)
