# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def get_names(a,b):
    c = []
    for x in a:
        for y in b:
            d = x + " " + y
            c.append (d)
    return c
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']


def average_scores(a):
    b = []
    for x in a:
        d = []
        e = 0
        for y in x:
            if y[1] == 0:
                c = y[0]
            elif y[1] == 1:
                c = y[0] * .9
            elif y[1] == 2:
                c = y[0] * .75
            elif y[1] == 3:
                c = y[0] * .5
            else: c = 0
            d.append (c)
        for z in d:
            e += z
        e = e/len(d)
        b.append (e)
    return b
