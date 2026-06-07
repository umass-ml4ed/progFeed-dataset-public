# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst: list):
    count = {}
    for i in lst:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1

    most_frequent = None
    large_count = 0
    for key in count:
        if count[key] > large_count:
            large_count = count[key]
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

def greet_user(users, id , default_lang = "en" , default_age = 18):
    if id not in users:
        return "User not found."
    name  = users[id]["name"]

    if "language" in users[id]:
        lang = users[id]["language"]
    else:
        lang = default_lang

    if "age" in users[id]:
        age = users[id]["age"]
    else:
        age = default_age

    if age < 18:
        if lang =="en":
            return f'Hey there, {name}!'
        elif lang == "es":
            return f"¡Hola, pequeño/a {name}!" 
        else:
            return f"Salut, {name}!"
        
    if lang == "en":
        return f'Hello, {name}!'
    elif lang == "es":
        return f'Hola, {name}!'
    else:
        return f'Bonjour, {name}!'
    
users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}  # Missing info
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
