# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def print_stars_to_file(n):

    #shitfart = #

    ##file_base = './2025_11_7_lab09/stars_'
    #file_new = file_base + str(n)
    #file_newer = file_new + ('.txt')
    whatever = open(f'./2025_11_7_lab09/stars_{n}.txt', 'x') 
    #str(file_newer), 'x')
    whatever.close()



    whatever2 = open(f'./2025_11_7_lab09/stars_{n}.txt', 'w')
    
    thingy = tuple(range(n))
    new_thingy = tuple(x + 1 for x in thingy)

    #i = 0 
    for number in new_thingy: 
        #i += 1
        whatever2.write(
            (' '*(n-number)) + ('*'*((2*number)-1)) + ('\n')
        )
    
    whatever2.close()

print_stars_to_file(4)