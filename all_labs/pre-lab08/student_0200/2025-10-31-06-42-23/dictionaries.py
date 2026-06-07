# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def most_frequent_element(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else: 
            count[i] = 1
    counts = 0
    most_frequent = None
    for key in count:
        if count[key] > counts:
            counts = count[key]
            most_frequent = key

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
    user_pref = users[user_id]
    name = user_pref.get("name", "User")
    language = user_pref.get("language", default_lang)
    age = user_pref.get("age", default_age)
    greetings = {"en": (f"Hello, {name}!", f"Hey there, {name}!"), "es": (f"Hola, {name}!", f"¡Hola, pequeño/a {name}!"), "fr": (f"Bonjour, {name}!", f"Salut, {name}!")}
    if language not in greetings:
        language = default_lang
    adult_greet, child_greet = greetings[language]
    if age < 18:
        return child_greet
    else:
        return adult_greet
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
