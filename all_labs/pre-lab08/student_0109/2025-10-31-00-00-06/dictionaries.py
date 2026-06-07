#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def most_frequent_element(lst):
    if not lst:
        return None
    dct = {e:0 for e in lst}
    for e in lst:
        dct[e] += 1
    count = [dct[key] for key in dct]
    for key in dct:
        if dct[key] == max(count):
            return key

users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}  # Missing info
}
