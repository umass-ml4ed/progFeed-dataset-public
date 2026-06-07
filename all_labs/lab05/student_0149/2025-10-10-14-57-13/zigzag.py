# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    for i in range(1, len(list) - 1):
        print(f"i: {i}")
        print(f"element: {list[i]}")
    return None
    variable = 0
    for thing in list:
        if variable == 0 or list[variable] == list[-1]:
            variable += 1
            continue
        # if (thing > list[(variable - 1)] and (thing > list[(variable + 1)])) or (thing < list[(variable - 1)] and (thing < list[(variable + 1)])):

print(is_zigzag([9, 8, 7, 6, 5]))