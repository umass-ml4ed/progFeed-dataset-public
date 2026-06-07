# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

apple=int(input('Enter total apples: '))
basket=int(input('Enter number of baskets: '))
perb=apple//basket
remain=apple%basket
print(f'For {apple} apples \nand {basket} baskets, there are: \n{perb} apples per basket \nwith {remain} apples leftover.')