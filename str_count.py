


def str_count(s,sub):
    
    if len(s) < len(sub):
        return 0


    if s[:len(sub)] == sub:
        return 1 + str_count(s[len(sub):])
    else:
        return str_count(s[1:])



