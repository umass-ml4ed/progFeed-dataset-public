# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_elements(lst):
    if not lst:
        return None
    counts = {}
    for thing in lst: 
        counts[thing] = counts.get(thing, 0) + 1
    return max(counts.values())

def greet_user(users, user_id, default_lang = "en", default_age = 18):
    if user_id not in users:
        return "User not found"
    
    user = users[user_id]
    name = user.get("name", "User")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)

    greetings = {
        "en": ("Hello, {name}", "Hey there, {name}"),
        "es": ("Hola, {name}", "¿Qué tal, {name}?"),
        "fr": ("Bonjour, {name}", "Salut, {name}!"),
        "de": ("Hallo, {name}", "Hey, {name}!")
    }

    adult_greeting, child_greeting = greetings.get(lang, greetings[default_lang])
    return (child_greeting if age < 18 else adult_greeting).format(name=name)