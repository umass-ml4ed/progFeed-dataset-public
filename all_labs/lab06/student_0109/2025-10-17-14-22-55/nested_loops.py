#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def get_names(fn,ln):
    full_names = []
    for i in fn:
        for j in ln:
            full_names.append(f'{fn} {ln}')
    return full_names
