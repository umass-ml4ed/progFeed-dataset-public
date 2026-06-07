def print_stars_to_file(n):
    z = str(n)
    x = ("stars_"+z+".txt")
    with open(x, "w") as file:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            file.write(' ' * spaces + '*' * stars +'\n')

print_stars_to_file(5)