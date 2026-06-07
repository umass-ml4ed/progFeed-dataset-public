# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

def most_frequent_element(lst):
    if not lst:
        return None
    
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1

    # Return the element with the highest count
    return max(counts, key=counts.get)


def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."

    info = users[user_id]
    name = info.get("name", "User")
    lang = info.get("language", default_lang)
    age = info.get("age", default_age)

    greetings = {
        "en": ("Hello, {name}!", "Hey there, {name}!"),
        "es": ("Hola, {name}!", "¡Hola, pequeño/a {name}!"),
        "fr": ("Bonjour, {name}!", "Salut, {name}!")
    }

    adult_greet, child_greet = greetings.get(lang, greetings["en"])
    return child_greet.format(name=name) if age < 18 else adult_greet.format(name=name)
