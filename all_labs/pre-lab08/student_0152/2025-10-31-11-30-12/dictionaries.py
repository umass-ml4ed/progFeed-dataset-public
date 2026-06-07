# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(list):
    elements = {}
    for element in list:
        if list == []:
            return None
        if element not in elements:
            elements[element] = 1
        elif element in elements:
            elements[element] += 1
    return sorted(elements, key = elements.get, reverse = True)[0]

#print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
#print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
#print(most_frequent_element([1, 2, 3, 4]))
print(most_frequent_element([]))