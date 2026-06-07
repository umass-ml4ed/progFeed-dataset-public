# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# Below, please implement the ab_func() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----

def ab_func(a,b):
    c = str(a)
    d = str(b)
    multi1 = c * b
    multi2 = d * a
    result = multi1 + multi2
    return str(result)

# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following lines (i.e. remove the # characters on each line)
# to test ab_func()
print(ab_func(5, 3))
print(ab_func(4, 7))
