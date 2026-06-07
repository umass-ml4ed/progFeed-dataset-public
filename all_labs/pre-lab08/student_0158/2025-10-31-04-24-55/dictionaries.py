# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lih):
    dih={}
    if len(lih)==0:
        return None
    else:
        for i in lih:
            if i not in dih:
                dih[i]=lih.count(i)
    return max(dih, key=dih.get)

def greet_user(users, user_id, default_lang='en', default_age=18):
    if user_id not in users:
        return "User not found."
    if 'language' in users[user_id]:
        lang=users[user_id]['language']
    else:
        lang=default_lang
    if 'age' in users[user_id]:
        age=users[user_id]['age']
    else:
        age=default_age
    if lang=='en' and age>=18:
        return f"Hello, {users[user_id]['name']}!"
    elif lang=='en' and age<18:
        return f"Hey there, {users[user_id]['name']}!"
    elif lang=='es' and age>=18:
        return f"Hola, {users[user_id]['name']}!"
    elif lang=='es' and age<18:
        return f"¡Hola, pequeño/a {users[user_id]['name']}!"
    elif lang=='fr' and age>=18:
        return f"Bonjour, {users[user_id]['name']}!"
    elif lang=='fr' and age<18:
        return f"Salut, {users[user_id]['name']}!"