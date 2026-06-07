# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not list:
        return None
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)

def greet_user(users, user_id, default_lang = "en", default_age = 18):
    if user_id not in users: 
        return "User not found."
    user = users[user_id]
    name = user.get('name', 'User')
    lang = user.get('language', default_lang)
    age = user.get('age', default_age)
    greeting_options = {
        'en': 'Hello',
        'es': 'Hola',
        'de': 'Hallo'
        }
    greeting = greeting_options.get(lang, greeting_options[default_lang])
    return f"{greeting}, {name}! You are {age} years old."
    