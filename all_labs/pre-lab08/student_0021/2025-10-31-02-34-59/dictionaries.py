# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    """Return the most frequent element in a list, or None if empty."""
    if not lst:
        return None
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    max_count = max(counts.values())
    for key, value in counts.items():
        if value == max_count:
            return key


def greet_user(users, user_id, default_lang="en", default_age=18):
    """Return a greeting for a user based on their language and age."""
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

    adult_greet, child_greet = greetings.get(lang, greetings["en"])
    return child_greet.format(name=name) if age < 18 else adult_greet.format(name=name)

