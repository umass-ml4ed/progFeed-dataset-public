# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apple_number = int(input('How many apples are there:\n'))

basket_number = int(input('How many baskets are there:\n'))

def divide_apples(apple_number, basket_number):
    apples_per_basket = apple_number // basket_number
    leftover = apple_number % basket_number
    print(f'You have {apple_number} apples.')
    print(f'You have {basket_number} baskets.')
    print(f'There will be {apples_per_basket} apples per basket.')
    print(f'{leftover} apples will be leftover.')
    return None

divide_apples(apple_number,basket_number)