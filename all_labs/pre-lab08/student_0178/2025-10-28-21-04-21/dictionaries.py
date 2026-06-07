# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(l):
    l1=[]
    l2={}
    if l==[]:
        return None
    else:
        for i in l:
            if i not in l1:
                l1.append(i)
        for i in l1:
            l2[i]=l.count(i)
        l3=sorted(l2.items(), key=lambda item:item[1])
        return l3[-1][0]
        
def greet_user(user, k):
    if k not in user:
        return f"User not found."
    else:
        d1=user[k]
        name=d1["name"]
        if "language" not in user or d1["language"]=='es':
            if "age" not in user:
                return f"Hola, {name}!"
            else:
                if d1["age"]<18:
                    return f"¡Hola, pequeño/a {name}!"
                else:
                    return f"Hola, {name}!"
        elif d1["language"]=='en':
            if "age" not in user:
                return f"Hello, {name}!"
            else:
                if d1["age"]<18:
                    return f"Hey there, {name}!"
                else:
                    return f"Hello, {name}!"
        elif d1["language"]=='fr':
            if "age" not in user:
                return f"Bonjour, {name}!"
            else:
                if d1["age"]<18:
                    return f"Salut, {name}!"
                else:
                    return f"Bonjour, {name}!"

  
