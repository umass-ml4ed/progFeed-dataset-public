# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    dict = {}
    for x in lst:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    return max(dict.values())

def greet_user(users, user_id, default_lang = "en", default_age = "18"):
    if user_id not in users:
        return "User not found."
    if default_lang == "en":
        if users["age"] < 18:
            return f"Hey there, {users["name"]}!"
        else:
            return f"Hello, {users["name"]}!"
    elif default_lang == "es":
        if users["age"] < 18:
            return f"¡Hola, pequeño/a {users["name"]}!"
        else:
            return f"Hola, {users["name"]}!"



