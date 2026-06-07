# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(a):
    x={}
    for i in a:
        if i not in x:
            x[i]=1
        else:
            x[i]+=1
    if x=={}:
        return None
    y=max(x, key=x.get)
    return(y)

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2
print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'
print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)
print(most_frequent_element([]))
# None


#"en"
#"Hello, {name}!"
#"Hey there, {name}!"
#"es"
#"Hola, {name}!"
#"¡Hola, pequeño/a {name}!"
#"fr"
#"Bonjour, {name}!"
#"Salut, {name}!"
#
#
#def greet_user(d):
#    x=[]
#    print()
#
#
#users = {
#    "u1": {"name": "Alice", "language": "en", "age": 25},
#    "u2": {"name": "Carlos", "language": "es", "age": 12},
#    "u3": {"name": "Marie", "language": "fr"},
#    "u4": {"name": "UnknownUser"}  # Missing info
#}
#print(greet_user(users, "u1"))
## Hello, Alice!
#print(greet_user(users, "u2"))
## ¡Hola, pequeño/a Carlos!
#print(greet_user(users, "u3"))
## Bonjour, Marie!   (default_age=18 → adult greeting)
#print(greet_user(users, "u4", default_lang="es"))
## Hola, UnknownUser!   (uses default language)
#print(greet_user(users, "u5"))
## User not found.