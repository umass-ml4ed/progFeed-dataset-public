# Author : REDACTED
# Email  : REDACTED
# Spire ID : REDACTED

#Take a list of elements, Return the element that appears most frequently in the list.
#If there are multiple elements with the same highest frequency, return any one of them.
def most_frequent_element(lst):
    if not lst:
        return None
    counts = {}  
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    max_count = 0
    most_frequent = None
    for key in counts:
        if counts[key] > max_count:
            max_count = counts[key]
            most_frequent = key
    return most_frequent

#function that greets a user based on their stored information in a nested dictionary.
def greet_user(users, user_id, default_lang, default_age):
    default_age=18
    default_lang="en"
    if user_id not in users:
        return "User not found."
    
    user = users[user_id]
    name = user["name"] if "name" in user else "Unknown"
    language = user["language"] if "language" in user else default_lang
    age = user["age"] if "age" in user else default_age

    if age < 18:
        if language == "es":
            return "¡Hola, pequeño/a " + name + "!"
        elif language == "fr":
            return "Salut, " + name + "!"
        else:
            return "Hey there, " + name + "!"
    else:
        if language == "es":
            return "Hola, " + name + "!"
        elif language == "fr":
            return "Bonjour, " + name + "!"
        else:
            return "Hello, " + name + "!"


