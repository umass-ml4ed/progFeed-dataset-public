# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def most_frequent_element(lst):
    """Return the most frequent element in the list, or None if empty."""
    if not lst:
        return None

    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1

    return max(counts, key=counts.get)

def greet_user(users, user_id, default_lang="en", default_age=18):
    """Return a personalized greeting based on user info."""
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

    # Pick correct language or fall back to English
    adult_greet, child_greet = greetings.get(lang, greetings["en"])

    if age < 18:
        return child_greet.format(name=name)
    else:
        return adult_greet.format(name=name)
