# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def divide_apples():
    totalApples= int(input("Total number of apples: "))
    totalBaskets= int(input("Total number of baskets: "))
    print(str(totalApples) + " apples for")
    print(str(totalBaskets) + " baskets can be divided as:")
    print(str(totalApples//totalBaskets) + " apples per basket, and ")
    print(str(totalApples % totalBaskets) + " leftover apples.")

divide_apples()
