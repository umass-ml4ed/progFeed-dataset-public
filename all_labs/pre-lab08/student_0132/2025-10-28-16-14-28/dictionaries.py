# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(l):
    freq = {}
    for i in l:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return  max(freq, key=freq.get)

def greet_user(users,user_id,default_lang = "en",default_age = 18):
    if user_id not in users:
        return "User not found."
    name = users[user_id].get("name", "user")
    lang = users[user_id].get("language", default_lang)
    age = users[user_id].get("age", default_age)
    child = False
    if age < 18:
        child = True
    if lang == "en":
        if child:
            return f"Hey there, {name}!"    
        else:
            return f"Hello, {name}!"
    if lang == "es":
        if child:
            return f"¡Hola, pequeño/a {name}!"
        else:
            return f"Hola, {name}!"
    if lang == "fr":
        if child:
            return f"Salut, {name}!"
        else:
            return f"Bonjour, {name}!"



