# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(list):
    item_count = {}
    for i in list:
        if i in item_count:
            item_count[i] += 1
        else:
            item_count[i] = 1
    highest_count = 0
    most = None
    for i in item_count:
        if item_count[i] > highest_count:
            highest_count = item_count[i]
            most = i
    return most

def greet_user(users, user_id, default_lang='en', default_age=18):
    if user_id not in users:
        return "User not found."
    if "language" in users[user_id]:
        language = users[user_id]["language"]
    else:
        language = default_lang
    if "age" in users[user_id]:
        age = users[user_id]["age"]
    else:
        age = default_age
    child = age < 18
    match (language, child):
        case ("en", False):
            return f"Hello, {users[user_id]["name"]}!"
        case ("en", True):
            return f"Hey there, {users[user_id]["name"]}!"
        case ("es", False):
            return f"Hola, {users[user_id]["name"]}!"
        case ("es", True):
            return f"¡Hola, pequeño/a {users[user_id]["name"]}!"
        case ("fr", False):
            return f"Bonjour, {users[user_id]["name"]}!"
        case ("fr", True):
            return f"Salut, {users[user_id]["name"]}!"