# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


def count_words(words):
    some_dict = {}
    for word in words:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict

words = ('umass', 'rhianna', 'seventeen', 'celery')
print(count_words(words))


    
    
    

    
