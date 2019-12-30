



def count_pairs(s):

    if len(s) <= 2:
        return 0



    return (1 if s[0] == s[2] else 0) + count_pairs(s[1:])
