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
def greet_user(users: dict, greet_user, default_age=18, default_lang="en"):
    if greet_user not in users:
        return "User not found."
    
    dct = users[greet_user]
    name = dct.get("name", "User")
    lang = dct.get("language", default_lang)
    age = dct.get("age", default_age)
    try:
        age = int(age)
    except (ValueError, TypeError):
        age = default_age

    if lang == "en":
        return f"Hello, {name}!" if age >= 18 else f"Hey there, {name}!"
    elif lang == "es":
        return f"Hola, {name}!" if age >= 18 else f"¡Hola, pequeño/a {name}!"
    elif lang == "fr":
        return f"Bonjour, {name}!" if age >= 18 else f"¡Salut, {name}!"
    else:
        return f"Hello, {name}!"



        