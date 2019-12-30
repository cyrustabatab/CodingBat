


def count_abc(s):

    if len(s) < 3:
        return 0

    return 1 + count_abc(s[1:]) if s[:3] == 'abc' or s[:3] == 'aba' else count_abc(s[1:])







        
