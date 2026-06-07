# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(l):
    if not l:
        return None
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    count=0

    for key in d:
        if d[key]>count:
            count=d[key]
            frequent=key

    return frequent



def greet_user(users, user_id, default_lang='en', default_age=18):
    if user_id not in users:
        return "User not found."
    user=users[user_id]
    
    if "name" in user:
        name =user["name"]
    
    if "language" in user:
        language=user["language"]
    else:
        language=default_lang
    
    if "age" in user:
        age= user["age"]
    else:
        age=default_age

        
    greeting={"en":{"adult": "Hello, ", "child": "Hey there, "}, 
              "es": {"adult":"Hola, ", "child": "¡Hola, pequeño/a "}, 
              "fr": {"adult": "Bonjour, ", "child": "Salut, "}}
    
    if age>=18:
        greetingp=greeting[language]["adult"]+ name+"!"
    else:
        greetingp=greeting[language]["child"]+ name +"!"

    return greetingp

users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}  # Missing info
}

print(greet_user(users, "u1"))
print(greet_user(users, "u2"))
print(greet_user(users, "u3"))
print(greet_user(users, "u4", default_lang="es"))
print(greet_user(users, "u5"))
