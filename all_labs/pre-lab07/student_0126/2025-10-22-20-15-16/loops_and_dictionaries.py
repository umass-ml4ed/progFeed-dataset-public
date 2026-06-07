# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

# def pyramid(n):
#     f = []
#     for i in range(n):
#         d = []
#         for j in range(n - i):    
#             if j < (n - i - 1):
#                 d.append(str(n - i - j) + ' ')
#             else:
#                 d.append(str(n - i - j))
#         f.append(str(''.join(d)))
#         f.append('\n')
#     a = ''.join(f)
#     return a

def pyramid(n):
    d = ''
    for i in range(n):
        for j in range(n - i):
            d += str(n - i - j)
            if (j < n - i - 1) and not (i == n - 1):
                d += ' '
        if i < (n - 1):
            d += '\n'
    return d
# print(pyramid(5))

# def merge_dicts(d1, d2):
#     m = {}
#     for i in d1:
#         m[i] = d1[i]
#         if i in d2:
#             m[i] += d2[i]
#             del d2[i]
#     for i in d2:
#         m[i] = d2[i]
#     print(m)

def merge_dicts(d1, d2):
    m = d1.copy()
    for i in d2:
        if i in d1:
            m[i] = (d2[i] + d1[i])
        else:
            m[i] = d2[i]
    return m
