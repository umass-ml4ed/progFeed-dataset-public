# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    dict = {}
    for i in lst:
        if (i in dict):
            dict[i] += 1
        else:
            dict[i] = 1
    most = None
    highest = 0
    for j in dict:
        if (dict[j] > highest):
            highest = dict[j]
            most = j
    return most

def greet_user(dict, user):
    if (user not in dict):
        return "User not found"
    greet = ""   
    if ("language" in dict[user]):
        d_lang = dict[user]["language"]
    else: 
        d_lang = "en"
    if ("age" in dict[user]):
        d_age = dict[user]["age"]
    else:
        d_age = 18
    if (d_lang == "en"):
        if (d_age < 18):
            greet = "Hey there, " + dict[user]["name"] + "!"
        else:
            greet = "Hello, " + dict[user]["name"] + "!"
    elif (d_lang == "es"):
        if (d_age < 18):
            greet = "¡Hola, pequeño/a " + dict[user]["name"] + "!"
        else:
            greet = "Hola, " + dict[user]["name"] + "!"
    elif (d_lang == "fr"):
        if (d_age < 18):
            greet = "Salut " + dict[user]["name"] + "!"
        else:
            greet = "Bonjour, " + dict[user]["name"] + "!"
    return greet




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

