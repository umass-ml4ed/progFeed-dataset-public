# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def pyramid(n):
    py =""
    for i in range (n):
        index = n-i;
        while (index>0):
            py = py + str(index)
            index = index -1
            if (index == 0): break
            py = py + " "
        py= py+ "\n"
    return py