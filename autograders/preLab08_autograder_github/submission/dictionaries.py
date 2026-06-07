def most_frequent_element(lst):
    if not lst:
        return None
    
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    
    max_key = max(counts, key=counts.get)
    return max_key

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."
    
    user = users[user_id]
    name = user.get("name", "User")
    language = user.get("language", default_lang)
    age = user.get("age", default_age)

    # Greeting templates
    greetings = {
        "en": ("Hello, {name}!", "Hey there, {name}!"),
        "es": ("Hola, {name}!", "¡Hola, pequeño/a {name}!"),
        "fr": ("Bonjour, {name}!", "Salut, {name}!")
    }

    # Select language or fallback
    if language not in greetings:
        language = default_lang

    adult_greet, child_greet = greetings[language]
    template = child_greet if age < 18 else adult_greet

    return template.format(name=name)

if __name__ == "__main__":
    print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
    print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
    print(most_frequent_element([1, 2, 3, 4]))
    print(most_frequent_element([]))

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
