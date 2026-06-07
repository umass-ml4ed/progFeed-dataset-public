# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def most_frequent_element(lst):
    dct = {}
    if (len(lst) == 0):
        return  None
    else:
        for i in range (len(lst)):
            if lst[i] not in dct:
                dct[lst[i]] = 1
            else:
                dct[lst[i]] += 1
        max = 0
        for key, count in dct.items():
            if count > max:
                max = count
                max_value_item = key
        return max_value_item
def greet_user(users:dict, greet_user, default_lang="en", default_age = 18):
        if (greet_user in users):
            dct = users[greet_user]
            age = dct.get("age", default_age)
            lang = dct.get("language", default_lang)
            name = dct.get("name", "User")
            # print (type(age))
            try:
                age = int(age)
            except (ValueError, TypeError):
                age = default_age
            if (lang == "en"):
                if (age >= 18):
                    return (f"Hello, {name}!")
                else:
                    return (f"Hey there, {name}!")
            elif (lang == "es"):
                if (age >= 18):
                    return (f"Hola, {name}!")
                else:
                    return (f"¡Hola, pequeño/a {name}!")
            elif (lang == "fr"):
                if (age >= 18):
                    return (f"Bonjour, {name}!")
                else:
                    return (f"Salut, {name}!")
            else:
                return (f"Hello, {name}!")
        else:
            return "User not found."
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


        