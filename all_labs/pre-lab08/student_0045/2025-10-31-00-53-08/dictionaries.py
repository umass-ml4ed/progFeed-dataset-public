# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(lst: list):
    if not lst:
        return None
    dct = {}
    for item in lst:
        dct[item] = dct.get(item, 0) + 1

    count = 0
    frequent = None
    for item, number in dct.items():
        if number>count:
            count = number
            frequent = item

    return frequent

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."
    user = users[user_id]
    name = user.get("name", "UnknownUser")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)
    greetings = {
        "en" : {"adult": "Hello, {name}!", "child" : "Hey there, {name}!"},
        "es" : {"adult" : "Hola, {name}!", "child" : "¡Hola, pequeño/a {name}!"},
        "fr" : {"adult" : "Bonjour, {name}!", "child" : "Salut, {name}!"}
    }
    if age<18:
        greeting_used = greetings.get(lang, greetings[default_lang])["child"]
    else:
        greeting_used = greetings.get(lang, greetings[default_lang])["adult"]
    return greeting_used.format(name=name)

users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"} 
}

print(greet_user(users, "u1"))
