

def paren_bit(s):
    if not s:
        return s
    

    if s[0] == '(' and s[-1] == ')':
        return s

    
    if s[0] == '(':
        return paren_bit(s[:-1])
    elif s[-1] == ')':
        return paren_bit(s[1:])
    else:
        return paren_bit(s[1:-1])










