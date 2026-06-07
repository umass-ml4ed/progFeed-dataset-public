# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED


''' A year is a leap year if:
It is divisible by 4
BUT if it's also divisible by 100, then it's not a leap year
UNLESS it’s divisible by 400! Then it is a leap year.
Your Task: Write a function to determine if a year is a leap year using nested branching!
'''
def is_leap_year(y:int):
  if y % 4 == 0:
    if y % 100 == 0:
      if y % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

year = int(input("Enter a year: "))

if leap_year(year):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")

def list_leap_years(a, b):
    """
    Return a list of leap years between a and b (inclusive).
    Must use a while loop.
    """
    leap_years = []
    year = a  # start from 'a'

    while year <= b:
        if is_leap_year(year):
            leap_years.append(year)
        year += 1  # move to next year

    return leap_years