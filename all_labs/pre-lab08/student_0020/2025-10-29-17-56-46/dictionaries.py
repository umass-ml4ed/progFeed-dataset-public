# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(list):
    d=dict()
    if list==[]:
        return None
    for item in list:
        if item in d:
            d[item]+=1
        else:
            d[item]=1
    count=0
    item=""
    for k,v in d.items():
        if v>count:
            count=v
            item=k
    return item

def greet_user(users,user_id,default_lang="en",default_age=18):
    if user_id not in users:
        return "User not found."
    
    try:
        default_lang=users[user_id]["language"]
    except:
        default_lang="en"
    try:
        default_age=users[user_id]["age"]
    except:
        default_age=18


    if default_lang=="en":
        if default_age>=18:
            return(f"Hello, {users[user_id]["name"]}!")
        else:
            return(f"Hey there, {users[user_id]["name"]}!")

    elif default_lang=="es":
        if default_age>=18:
            return(f"Hola, {users[user_id]["name"]}!")
        else:
            return(f"¡Hola, pequeño/a {users[user_id]["name"]}!")

    elif default_lang=="fr":
        if default_age>=18:
            return(f"Bonjour, {users[user_id]["name"]}!")
        else:
            return(f"Salut, {users[user_id]["name"]}!")
        