# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(elements):
    if not elements:
        return None

    counts = {}
    for item in elements:
        counts[item] = counts.get(item, 0) + 1

    max_element = max(counts, key=counts.get)
    return max_element


def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."

    user = users[user_id]
    name = user.get("name", "User")
    language = user.get("language", default_lang)
    age = user.get("age", default_age)

    greetings = {
        "en": ("Hello, {name}!", "Hey there, {name}!"),
        "es": ("Hola, {name}!", "¡Hola, pequeño/a {name}!"),
        "fr": ("Bonjour, {name}!", "Salut, {name}!")
    }

    adult, child = greetings.get(language, greetings["en"])
    return child.format(name=name) if age < 18 else adult.format(name=name)
