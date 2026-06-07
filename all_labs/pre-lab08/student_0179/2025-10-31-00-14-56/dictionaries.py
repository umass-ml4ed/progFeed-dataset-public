# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(elements):
    counts = dict()
    if elements == []:
        return None
    else:
        for element in elements:
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1
        largest_count = ""
        compare = 0
        for count in counts:
            if counts[count] > compare:
                compare = counts[count]
                largest_count = count
        return largest_count
    
print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
print(most_frequent_element([1, 2, 3, 4]))
