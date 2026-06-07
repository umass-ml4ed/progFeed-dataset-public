# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(elements):
    if not elements:
        return None

    freq = {}
    for item in elements:
        freq[item] = freq.get(item, 0) + 1

    max_item = max(freq, key=freq.get)
    return max_item

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."

    user = users[user_id]
    name = user.get("name", "User")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)

    greetings = {
        "en": ("Hello, {name}!", "Hey there, {name}!"),
        "es": ("Hola, {name}!", "¡Hola, pequeño/a {name}!"),
        "fr": ("Bonjour, {name}!", "Salut, {name}!")
    }

    if lang not in greetings:
        lang = default_lang

    adult_greet, child_greet = greetings[lang]
    if age < 18:
        return child_greet.format(name=name)
    else:
        return adult_greet.format(name=name)