# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(items):
    L={}
    for element in items:
        if element in L:
            L[element]+=1
        else:
            L[element]=1
    M=None
    N=-1
    for i in items:
        c=L[i]
        if c>N:
            N=c
            M=i
    return M

    if not items:
        return None

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
print(most_frequent_element([1, 2, 3, 4]))
print(most_frequent_element([]))

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."
    info=users[user_id]

    name=info.get("name", "UnknownUser")
    lang=info.get("language", default_lang)
    age=info.get("age", default_age)

    templates={
        "en": {"adult": "Hello, {name}!","child": "Hey there, {name}!"},
        "es": {"adult": "Hola, {name}!","child": "¡Hola, pequeño/a {name}!"},
        "fr": {"adult": "Bonjour, {name}!","child": "Salut, {name}!"},
    }

    if lang not in templates:
        lang=default_lang if default_lang in templates else "en"

    kind="child" if age < 18 else "adult"
    return templates[lang][kind].format(name=name)

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

