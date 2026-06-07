def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        for i in range(n,0,-1):
            f.write(" "*(i-1))
            f.write("*"*(2*(n-i+1)-1))
            f.write("\n")
print_stars_to_file(3)
def calc_avg_from_file():
    with open("grades.txt") as f:
        text = f.read()
        s = text.split("\n")

        avg = sum(list(map(float,s))) / len(s)

        return avg