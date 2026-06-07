totalApples = int(input("Enter total apples: "))
print(str(totalApples) + " apples for")

numberBaskets = int(input("Enter number of baskets: "))
print(str(numberBaskets) + " baskets can be divided as:")

def divide(x,y):
    #x = totalApples
    #y = numberBaskets
    div = x//y
    return div
result = divide(totalApples,numberBaskets)
print(str(result) + " apples per basket, and")

def remainder(a,b):
    mod = a%b
    return mod
res = remainder(totalApples,numberBaskets)
print(str(res) + " leftover apples.")