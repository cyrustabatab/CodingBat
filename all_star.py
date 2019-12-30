



def all_star(s):

    if len(s) <= 1:
        return s

    return (s[0] + "*") + all_star(s[1:])



