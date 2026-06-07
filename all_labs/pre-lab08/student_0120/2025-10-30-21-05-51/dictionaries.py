# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

def most_frequent_element(lst):
    if not lst:
        return None

    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1

    most_frequent = max(counts, key=counts.get)
    return most_frequent

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2

print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'

print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)

print(most_frequent_element([]))
# None

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."

    user = users[user_id]
    name = user.get("name", "User")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)

    greetings = {
        "en": {
            "adult": "Hello, {name}!",
            "child": "Hey there, {name}!"
        },
        "es": {
            "adult": "Hola, {name}!",
            "child": "¡Hola, pequeño/a {name}!"
        },
        "fr": {
            "adult": "Bonjour, {name}!",
            "child": "Salut, {name}!"
        }
    }

    if lang not in greetings:
        lang = "en"
    if age < 18:
        return greetings[lang]["child"].format(name=name)
    else:
        return greetings[lang]["adult"].format(name=name)

users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}  # Missing info
}
print(greet_user(users, "u1"))
# Hello, Alice!

print(greet_user(users, "u2"))
# ¡Hola, pequeño/a Carlos!

print(greet_user(users, "u3"))
# Bonjour, Marie!   (default_age=18 → adult greeting)

print(greet_user(users, "u4", default_lang="es"))
# Hola, UnknownUser!   (uses default language)

print(greet_user(users, "u5"))
# User not found.

