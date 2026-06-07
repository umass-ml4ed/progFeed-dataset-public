# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(a):
    if len(a) < 3:
        return True
    else:
        for item in a:
            location = a.index(item)
            if location == len(a) - 1:
                if item != a[location-1]:
                    return True
                else:
                    return False
            elif location == 0:
                if item > a[location+1] or item < a[location+1]:
                    continue
            else:
                if item > a[location-1] and item > a[location+1]:
                    continue
                elif item < a[location-1] and item < a[location+1]:
                    continue
                else:
                    return False
        return True

#evil spaghetti code, I know there's a better way to do this but I spent too long trying to get this to work and sunk cost fallacy wins 


# a = [1, 3, 2, 4, 3]

# location = a.index(1)

# print(a[location-1])
# print(a[location+1])

print(is_zigzag([1, 3, 2, 4, 3]))
print(is_zigzag([1, 4, 2, 5, 3]))
print(is_zigzag([1, 2, 3, 4]))
print(is_zigzag([10]))
print(is_zigzag([1, 3, 2, 4, 5]))

#zigzag = true if every element is either greater than or smaller than
# both its neighbors