# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
num_apples=int(input('Enter the number of apples: '))
num_basket=int(input('Enter the number of baskets: '))
app_per_basket=num_apples//num_basket
out_app=num_apples%num_basket
print(num_apples,' apples for')
print(num_basket,' baskets can be divided as:')
print(app_per_basket,' apples per basket, and')
print(out_app,'leftover apples:')