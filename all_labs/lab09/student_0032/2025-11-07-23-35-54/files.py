# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def print_stars_to_file(n: int):
    file_base = './2025_11_7_lab09/stars_'
    file_new = file_base + str(n)
    file_newer = file_new + ('.txt')
    whatever = open(str(file_newer), 'x')
    whatever.close()



    whatever2 = open(str(file_newer), 'w')
    
    thingy = tuple(range(n))
    new_thingy = tuple(x + 1 for x in thingy)

    #i = 0 
    for number in new_thingy: 
        #i += 1
        whatever2.write(
            (' '*(n-number)) + ('*'*((2*number)-1)) + ('\n')
        )
    
    whatever2.close()

    return True
    


    #contents = whatever.read()
    #print(contents)

print_stars_to_file(6)