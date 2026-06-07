# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not lst:
        return None
    
    counts = dict()
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    max_count = 0
    most_frequent = None
    for key, value in counts.items():
        if value > max_count:
            max_count = value
            most_frequent = key
    return most_frequent

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."
    
    user_info = users[user_id]
    name = user_info.get("name", "User")
    language = user_info.get("language", default_lang)
    age = user_info.get("age", default_age)
    
    greetings = {
        "en": {"adult": "Hello, {name}!", "child": "Hey there, {name}!"},
        "es": {"adult": "Hola, {name}!", "child": "¡Hola, pequeño/a {name}!"},
        "fr": {"adult": "Bonjour, {name}!", "child": "Salut, {name}!"},
    }
    if language not in greetings:
        language = default_lang
    
    if age < 18:
        return greetings[language]["child"].format(name=name)
    else:
        return greetings[language]["adult"].format(name=name)



print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2

print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'

print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)

print(most_frequent_element([]))
# None

