# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def most_frequent_element(elements):
    count = {}
    if not elements:
        return None

    for c in elements:
        count[c] = count.get(c, 0) + 1
    return max(count, key=count.get)


  

def greet_user(users, user_id, default_lang='en', default_age=18):
    
    if user_id not in users:
        return "User not found."
    userid = users[user_id]
    language = userid.get('language', default_lang)
    age = userid.get('age', default_age)
    name = userid['name']

    adult_greetings = {
        "en": "Hello, ",
        "es": "Hola, ",
        "fr": "Bonjour, "
    }
    child_greetings = {
        "en": "Hey there, ",
        "es": "¡Hola, pequeño/a ",
        "fr": "Salut, "
    }

    if age < 18:
        return child_greetings[language] + name + '!'
    else:
        return adult_greetings[language] + name + '!'
    


  

                
        



