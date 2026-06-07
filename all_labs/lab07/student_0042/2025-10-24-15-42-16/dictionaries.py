# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




def count_words(a):
    some_dict = {}
    for item in a:
        if item in some_dict:
            some_dict[item] += 1
        elif item not in some_dict:
            some_dict[item] = 1
    return some_dict

# def average_prices(a):
#     pricedict = {}

#     for item in a:
#         if item[0] in pricedict:
#             b = pricedict[item[0]]
#             pricedict[item[0]] = (b+item[1])/2
#         elif item not in pricedict:
#             pricedict[item[0]] = item[1]
#     return pricedict
#This one would have worked if each tuple only had a max of 2 of each item, but since it immediately averages rather than adding all the values together and then averaging, it doesn't work :(
#I saved this one (in case my other idea for how to do this didn't work) + copy and pasted it to make a new one

def average_prices(a):
    totaldict = {}
    dividict = {}
    pricedict = {}
    for item in a:
        if item[0] in totaldict:
            totaldict[item[0]] += item[1]
            dividict[item[0]] += 1
        elif item not in pricedict:
            totaldict[item[0]] = item[1]
            dividict[item[0]] = 1
    for item in totaldict:
        pricedict[item] = totaldict[item]/dividict[item]
    return pricedict

# def count_bigrams(a):
#     some_dict = {}
#     counter = 0
#     for item in a:
#         if counter+1 < len(a):
#             if f"{a[counter]}, {a[counter+1]}" in some_dict:
#                 some_dict[a[counter], a[counter+1]] += 1
#             elif f"{a[counter]}, {a[counter+1]}" not in some_dict:
#                 some_dict[a[counter], a[counter+1]] = 1
#         else:
#             continue
#         counter +=1
#thought of a better way to format this by making a temporary variable, but kept it in case I messed the code up and needed it later

def count_bigrams(a):
    some_dict = {}
    counter = 0
    for item in a:
        if counter+1 < len(a):
            temptuple = (item, a[counter+1])
            if temptuple in some_dict:
                some_dict[temptuple] += 1
            elif temptuple not in some_dict:
                some_dict[temptuple] = 1
        else:
            continue
        counter +=1
    return some_dict

