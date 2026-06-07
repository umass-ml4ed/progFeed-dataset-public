# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    ind = 1
    Zig = True
    if len(lst) < 3:
        Zig = True
    else:
        for nmber in lst[1:-1]:
            if ((nmber < lst[ind+1]) and (nmber < lst[ind-1])) or ((nmber > lst[ind+1]) and (nmber > lst[ind-1])):
                Zig = True
                ind += 1
            else:
                Zig = False
                break
    return Zig
