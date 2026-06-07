# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def large_root(a, b, c):
    x1 = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)
    x2 = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
    x = max(x1, x2)
    return float(x)
def quadSolver(large_root):
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    print(a, "* x^2 +", b, "* x +", c, "has larger root:")
    print(large_root(a, b, c))
quadSolver(large_root)
