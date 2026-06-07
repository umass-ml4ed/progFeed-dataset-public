# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(lst):
    dict={}
    for element in lst:
        if element in dict:
            dict[element]+= 1
        else:
            dict[element]=1
    highest_count=0
    most_frequent=None

    for element in dict:
        if dict[element]>highest_count:
            highest_count=dict[element]
            most_frequent=element
    
    return most_frequent

def greet_user(users, user_id, default_lang='en', default_age=18):    
    if user_id not in users:
        return('User not found.')
    user=users[user_id]
    if 'language' in user:
        lang=user['language']
    else:
        lang=default_lang
    if 'age' in user:
        age=user['age']
    else:
        age=default_age
    name=user['name']
    if lang=='en':
        if age<18:
            return(f'Hey there, {name}!')
        else:
            return(f'Hello, {name}!')
    if lang=='es':
        if age<18:
            return(f'¡Hola, pequeño/a {name}!')
        else:
            return(f'Hola, {name}!')
    if lang=='fr':
        if age<18:
            return(f'Salut, {name}!')
        else:
            return(f'Bonjour, {name}!')
        
users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"} 
}

print(greet_user(users, "u1"))
print(greet_user(users, "u2"))
print(greet_user(users, "u3"))
print(greet_user(users, "u4", default_lang="es"))
print(greet_user(users, "u5"))
