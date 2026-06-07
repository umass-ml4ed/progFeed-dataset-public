# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst:list):
    seen = {}
    for i in lst:
        if len(lst)==0:
            return None
        if i not in seen:
            seen[i]=1
        else:
            seen[i]+=1
    freq=[]
    for v in seen.values():
        freq.append(v)
    for key,value in seen.items():
        if value == max(freq):
            return key

def greet_user(users:dict,u,dlang="en",dage=18):
    if u not in users:
        return "User not found."
    ids=users[u]
    name=ids.get("name")
    language=ids.get("language",dlang)
    age=ids.get("age",dage)

    if language not in ("en","fr","es"):
        language=dlang
    

    if age >= 18:
        if language == "en":
            return f"Hello, {users[u]['name']}!"
        if language == "fr":
            return f"Bonjour, {users[u]['name']}!"
        if language == "es":
            return f"Hola, {users[u]['name']}!"
    if age < 18:
        if language == "en":
            return f"Hey there, {users[u]['name']}!"
        if language == "fr":
            return f"Salut, {users[u]['name']}!"
        if language == "es":
            return f"¡Hola, pequeño/a {users[u]['name']}!"
        
