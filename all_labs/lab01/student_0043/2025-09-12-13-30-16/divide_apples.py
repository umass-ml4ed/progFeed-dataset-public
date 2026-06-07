# REDACTED_NAME
# REDACTED_EMAIL
# REDACTED_SPIRE_ID
def divide_apples(apples, baskets):
    apples_per_basket = apples // baskets
    leftover_apples = apples % baskets
    print(f"{apples} apples for \r {baskets} baskets can be divided as: {apples_per_basket} apples per basket, and {leftover_apples} leftover apples.")
    return apples_per_basket, leftover_apples
apples = int(input("Enter total apples: "))
baskets = int(input("Enter total baskets: "))
divide_apples(apples, baskets)

