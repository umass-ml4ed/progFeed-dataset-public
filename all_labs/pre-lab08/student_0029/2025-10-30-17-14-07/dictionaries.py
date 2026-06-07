# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not list:
        return None
    frequency = {}
    for i in lst:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    most_frequent = lst[0]
    for key in frequency:
        if frequency[key] > frequency[most_frequent]:
            most_frequent = key

    return most_frequent

def greet_user(users, user_id, default_lang, default_age):
    if user_id not in users: 
        return "User not found"
    user = users[user_id]
    lang = user.get('language', default_lang)
    age = user.get('age', default_age)
    greeting_options = {
        'en': 'Hello',
        'es': 'Hola',
        'de': 'Hallo'
        }
    adult_greeting, child_greeting = greeting_options.get(lang, greeting_options[default_lang]), "Hey there"
    if age < 18:
        return child_greeting.format
    else:
        return adult_greeting
    