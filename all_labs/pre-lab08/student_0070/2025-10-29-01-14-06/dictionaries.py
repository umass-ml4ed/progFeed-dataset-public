# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not lst:
        return None
    
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent


def greet_user(users, user_id, default_lang="en", default_age=18):
    greetings = {
        "en": {"adult": "Hello, {name}!", "child": "Hey there, {name}!"},
        "es": {"adult": "Hola, {name}!", "child": "¡Hola, pequeño/a {name}!"},
        "fr": {"adult": "Bonjour, {name}!", "child": "Salut, {name}!"}
    }
    
    if user_id not in users:
        return "User not found."
    
    user_info = users[user_id]
    name = user_info.get("name", "User")
    language = user_info.get("language", default_lang)
    age = user_info.get("age", default_age)
    
    if language not in greetings:
        language = default_lang
    
    if age < 18:
        greeting_template = greetings[language]["child"]
    else:
        greeting_template = greetings[language]["adult"]
    
    return greeting_template.format(name=name)
