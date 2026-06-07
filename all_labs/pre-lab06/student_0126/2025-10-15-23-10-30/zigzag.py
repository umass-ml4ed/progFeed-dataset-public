# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

# def longest_zigzag_from_start(lst):
#     if len(lst) <= 2:
#         return len(lst)
#     t = 0
#     if lst[1] > lst[0]:
#         t = 1
#     for i in range(1, len(lst)):
#         if lst[i] < lst[i - 1]:
#             if t == 0:
#                 t = 1
#             else:
#                 return i
#         elif lst[i] > lst[i - 1]:
#             if t == 1:
#                 t = 0
#             else:
#                 return i
#         else: return i
#     return i + 1

def y(s, lst):
    if len(lst) - s <= 2:
        return len(lst) - s
    t = 0
    if lst[s + 1] > lst[s]:
        t = 1
    for i in range(s + 1, len(lst)):
        if lst[i] < lst[i - 1]:
            if t == 0:
                t = 1
            else:
                return i - s
        elif lst[i] > lst[i - 1]:
            if t == 1:
                t = 0
            else:
                return i - s
        else: return i - s
    return i + 1 - s

def longest_zigzag_from_start(lst):
    return y(0, lst)

def zigzag_lengths_from_all_starts(lst):
    t = []
    for i in range(len(lst)):
        t.append(y(i, lst))
    return t

