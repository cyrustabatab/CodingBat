



def count_11(s):

    if len(s) < 2:
        return 0


    return 1 + count_11(s[2:]) if s[:2] = 11 else count_11(s[1:])
