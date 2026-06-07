# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    dict = {}
    maximum = 0
    if len(lst) > 0:
        for element in lst:
            if element in dict:
                dict[element] = dict[element] + 1
            else:
                dict[element] = 1
        maximum = max(dict.values())
        for key in dict:
            if dict[key] == maximum:
                return key
    else:
        return None

def greet_user(users, user_id, default_lang="en", default_age=18):
    greetings = {
        "en": {"adult": "Hello, {name}!", "child": "Hey there, {name}!"},
        "es": {"adult": "Hola, {name}!", "child": "¡Hola, pequeño/a {name}!"},
        "fr": {"adult": "Bonjour, {name}!", "child": "Salut, {name}!"}
    }

    if user_id not in users:
        return "User not found."

    user = users[user_id]
    name = user.get("name", "Unknown")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)

    greet_type = "child" if age < 18 else "adult"
    lang_greetings = greetings.get(lang, greetings["en"])
    return lang_greetings[greet_type].format(name=name)
