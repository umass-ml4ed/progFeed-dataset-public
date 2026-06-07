# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ["Ari", "Taylor"]
last_names = ["Levine", "Lopez", "Khan", "Wang"]

def func1():
    list1 = [] 
    for x in first_names:
        for i in last_names:
            n = x + " " + i
            list1.append(n)
    return (list1)

print(func1())