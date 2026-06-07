a1 = int(input("Enter total apples: "))
a2 = int(input("Enter number of baskets: "))

a3 = (a1 // a2)
a4 = (a1 % a2)

a1 = str(a1)
a2 = str(a2)
print(a1 + " apples for")
print(a2 + " baskets can be divided as:")

a3 = str(a3)
a4 = str(a4)
print(a3,"apples per basket, and")
print(a4, "leftover apples.")