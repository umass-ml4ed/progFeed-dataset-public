# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(lst):
    if len(lst) == 0:
        return None
    
    count = {}
    
    for item in lst:
        if item in count:
            count[item] = count[item] + 1
        else:
            count[item] = 1

    most_freq = None
    highest_count = 0

    for item in count:
        if count[item] > highest_count:
            highest_count = count[item]
            most_freq = item

    return most_freq

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."
    
    user = users[user_id]
    name = user.get("name", "User")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)

    if lang == "en":
        if age < 18:
            return "Hey there, " + name + "!"
        else:
            return "Hello, " + name + "!"
    elif lang == "es":
        if age < 18:
            return "¡Hola, pequeño/a " + name + "!"
        else:
            return "Hola, " + name + "!"
    elif lang == "fr":
        if age < 18:
            return "Salut, " + name + "!"
        else:
            return "Bonjour, " + name + "!"
    else:
        if age < 18:
            return "Hey there, " + name + "!"
        else:
            return "Hello, " + name + "!"