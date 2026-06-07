# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(list):
    d={}
    for item in list:
        if item in d:
            d[item]+=1
        else:
            d[item]=1

    max_k=None
    max_v=0

    for k,v in d.items():
        if v>max_v:
            max_v=v
            max_k=k
    
    return max_k

def greet_user(users,user_id,default_lang="en",default_age=18):

    try:
        default_lang=users[user_id]["language"]
    except:
        pass

    try:
        default_age=users[user_id]["age"]
    except:
        pass

    try:
        if default_lang=="en":
            if default_age>=18:
                return(f"Hello, {users[user_id]["name"]}!")
            else:
                return(f"Hello, {users[user_id]["name"]}!")
       
        elif default_lang=="es":
            if default_age>=18:
                return(f"Hola, {users[user_id]["name"]}!")
            else:
                return(f"¡Hola, pequeño/a  {users[user_id]["name"]}!")

        elif default_lang=="fr":
            if default_age>=18:
                return(f"Bonjour, {users[user_id]["name"]}!")
            else:
                return(f"Salut, {users[user_id]["name"]}!")
    except:
        return("User not found.")