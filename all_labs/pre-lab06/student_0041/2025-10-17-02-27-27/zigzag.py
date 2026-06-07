# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if(2 > len(lst)):
        return len(lst)

    if(lst[1] > lst[0]):
        previous = "up"
    else:
        previous = "down"

    count = 2 # since it cannot be shorter than 2

    for index in range(1,len(lst)-1):
        if(lst[index + 1] > lst[index]):
            current = "up"
        elif(lst[index + 1] < lst[index]):
            current = "down"

        if(previous == "up" and current == "down"):
            count += 1
            previous = current # to switch
        elif(previous == "down" and current == "up"):
            count += 1
            previous = current
        else:
            break
    return count


print(longest_zigzag_from_start([1, 3, 2, 4, 3]))
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))


def zigzag_lengths_from_all_starts(lst):
    mylist = []

    if(len(lst) < 2):
        return [len(lst)]

    for i in range(len(lst)):
        count = 2

        if i == len(lst) - 1: # last element
            mylist.append(1)
        else:
            if(lst[i+1] != lst[i]):
                if(lst[i+1] > lst[i]): # inside the for loop bc each element will change for i (in nested loops)
                    previous = "up"
                else:
                    previous = "down" # 2 elements in zig zag so far
                #count = 2

                for j in range(i+1, len(lst)-1):
                    if(lst[j + 1] > lst[j]):
                        current = "up"
                    elif(lst[j + 1] < lst[j]):
                        current = "down"
                    else:
                        break

                    if(previous == "up" and current == "down"):
                        previous = current
                    elif(previous == "down" and current == "up"):
                        previous = current
                    else:
                        break

                    count += 1

                mylist.append(count)
            else:
                mylist.append(1)

    return mylist

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))      # [5, 4, 3, 2, 1]
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))      # [2, 2, 2, 2, 1]
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))   # [5, 4, 3, 2, 2, 1]
print(zigzag_lengths_from_all_starts([10]))                 # [1]