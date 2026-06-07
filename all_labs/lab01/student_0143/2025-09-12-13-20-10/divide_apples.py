# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input('Enter total apples: '))
baskets = int(input('Enter number of baskets: '))

import math

print(f'{apples} apples for'
      f'\n{baskets} baskets can be divide as: '
      f'\n{math.floor(apples/baskets)} apples per basket, and'
      f'\n{apples % baskets} leftover apples')