#1 Implement most_frequent_element
def most_frequent_element(lst):
    if not lst:
        return None
    count ={}
    for item in lst:
        count[item] = count.get(item, 0) + 1
    return max(count, key = count.get)

#2 
def greet_user(users, user_id, default_lang = "en", default_age = 18):
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
    return (child_greet if age < 18 else adult_greet).format(name = name)

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