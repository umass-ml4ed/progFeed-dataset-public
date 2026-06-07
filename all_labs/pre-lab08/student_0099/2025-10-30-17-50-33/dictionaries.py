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


def greet_user(users, user_id, default_lang="en", default_age=18):

    
    if user_id not in users:
        return "User not found."

    user = users[user_id]
    
    
    name = user.get("name", "User")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)

    
    greetings = {
        "en": {
            "adult": "Hello, {name}!",
            "child": "Hey there, {name}!"
        },
        "es": {
            "adult": "Hola, {name}!",
            "child": "¡Hola, pequeño/a {name}!"
        },
        "fr": {
            "adult": "Bonjour, {name}!",
            "child": "Salut, {name}!"
        }
    }

    
    lang_greetings = greetings.get(lang, greetings["en"])

    
    if age < 18:
        return lang_greetings["child"].format(name=name)
    else:
        return lang_greetings["adult"].format(name=name)

