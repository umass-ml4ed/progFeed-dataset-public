# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not lst:
        return None
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    most_frequent = max(counts, key=counts.get)
    return most_frequent
print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
print(most_frequent_element([1, 2, 3, 4]))
print(most_frequent_element([]))

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."
    user_info = users[user_id]
    name = user_info.get("name", "User")
    lang = user_info.get("language", default_lang)
    age = user_info.get("age", default_age)
    greetings = {
        "en": ("Hello, {name}!", "Hey there, {name}!"),
        "es": ("Hola, {name}!", "¡Hola, pequeño/a {name}!"),
        "fr": ("Bonjour, {name}!", "Salut, {name}!")
    }
    if lang not in greetings:
        lang = default_lang
    adult_greet, child_greet = greetings[lang]
    return child_greet.format(name=name) if age < 18 else adult_greet.format(name=name)
users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}  # Missing info
}
print(greet_user(users, "u1"))
print(greet_user(users, "u2"))
print(greet_user(users, "u3"))
print(greet_user(users, "u4", default_lang="es"))
print(greet_user(users, "u5"))
