# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def count_words(words):
    some_dict={}
    k=0
    for i in range (len(words)):
        if (words[i] not in some_dict):
            # some_dict[words[i]] = words[i]
            some_dict[words[i]] = 1
            k +=1
        else:
            some_dict[str(words[i])]+=1
    return some_dict

def average_price(tup):
    unique_list = []
    for i in range (1,len(tup)):
        if (tup[i][0] not in unique_list):
            unique_list.append(tup[i][0])
    # return (unique_list)
    sum_of_uni_val=[]
    sum_val=[]
    for i in range (len(unique_list)):
        sum_of_uni_val.append(0)
        sum_val.append(0)
    for i in range (len(unique_list)):
        for j in range (len(tup)):
            if (tup[j][0] == unique_list[i]):
                sum_of_uni_val[i] += tup[j][1]
                sum_val[i]+=1
    # create set
    some_dict={}
    for i in range (len(unique_list)):
        # some_dict[unique_list[i]] = unique_list[i]
        some_dict[unique_list[i]] = sum_of_uni_val[i]/sum_val[i]
    return some_dict

# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_price(prices))
def count_bigrams(tup):
    if (len(tup)<=1):
        return {}
    bigrams =[]
    for i in range (len(tup)-1):
        new_list = []
        new_list.append(tup[i])
        new_list.append(tup[i+1])
        bigrams.append(new_list)
    for i in range (len(bigrams)):
        uni_list=[]
        uni_val=[]
        for i in range (len(bigrams)):
            if bigrams[i] not in uni_list:
                uni_list.append(bigrams[i])
    for i in range (len(uni_list)):
        uni_val.append(0)
    for i in range (len(uni_list)):
        for j in range(len(bigrams)):
            if (bigrams[j]==uni_list[i]):
                uni_val[i]+=1
    some_dict={}
    for i in range (len(uni_list)):
        if (bigrams[i] in uni_list):
            # some_dict[tuple(uni_list[i])] = tuple(uni_list[i])
            some_dict[tuple(uni_list[i])] = uni_val[i]
    return some_dict
        


# words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
# print(count_bigrams(words))



