# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open("stars_" + str(n) + ".txt", "w") as file: # when the "with" block ends, the file automatically closes
    # the w is the writing mode
        for i in range(1,n+1): # since n is exclusive
            spaces = n-i
            stars = 2*i-1
            line = (" " * spaces) + ("*" * stars)
            file.write(line + "\n") # replaces print(line)

# line = [(" " * (n-i)) + ("*" * (2*i-1)) for i in range(1,n+1)] --> list comphresion ver.

print_stars_to_file(3)

def calc_avg_from_file():
    with open("grades.txt", "r") as file: # r is the reading mode
        text = file.read()
        lst = text.split("\n")
        grades = [float(g) for g in lst] # list comphrehension otherwise i would need to call it as a helper func
        average = sum(grades)/len(grades)
        # cannot cast "grades" directly since python can't convert all items in a list to a float
        return average # since this is a "read" file, not a write one