



def string_clean(s):
    if len(s) <= 1:
        return s


    return string_clean(s[1:]) if s[0] == s[1] else s[0] + string_clean(s[1:])


