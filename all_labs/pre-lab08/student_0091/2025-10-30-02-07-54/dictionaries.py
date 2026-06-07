# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

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

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2

print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'

print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)

print(most_frequent_element([]))
# None



def greet_user(users, user_id, default_lang="en", default_age=18):

    if user_id not in users:
        return "User not found."

    user = users[user_id]


    if "name" in user:
        name = user["name"]
    else:
        name = "User"

    if "language" in user:
        language = user["language"]
    else:
        language = default_lang

    if "age" in user:
        age = user["age"]
    else:
        age = default_age


    if language == "en":
        if age < 18:
            greeting = "Hey there, " + name + "!"
        else:
            greeting = "Hello, " + name + "!"
    elif language == "es":
        if age < 18:
            greeting = "¡Hola, pequeño/a " + name + "!"
        else:
            greeting = "Hola, " + name + "!"
    elif language == "fr":
        if age < 18:
            greeting = "Salut, " + name + "!"
        else:
            greeting = "Bonjour, " + name + "!"
    else:
        if age < 18:
            greeting = "Hey there, " + name + "!"
        else:
            greeting = "Hello, " + name + "!"

    return greeting
users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}
}


print(greet_user(users, "u1"))
# Hello, Alice!

print(greet_user(users, "u2"))
# ¡Hola, pequeño/a Carlos!

print(greet_user(users, "u3"))
# Bonjour, Marie!   (default_age=18 → adult greeting)

print(greet_user(users, "u4", default_lang="es"))
# Hola, UnknownUser!   (uses default language)

print(greet_user(users, "u5"))
# User not found.

