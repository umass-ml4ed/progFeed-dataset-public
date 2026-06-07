# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
apples_number=int(input("number of apples you want?"))
apples_basket=int(input("number of baskets you need?"))
print(f"there are {apples_number} apples" )
print(f"you have chosen {apples_basket} buckets")
applesper_basket=apples_number//apples_basket
apples_left=apples_number%apples_basket
print(f"which would result in {applesper_basket} apples in each basket")
print(f"resulting in {apples_left} apples left")