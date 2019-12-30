


def nest_paren(s):

    if not s:
        return True

    if s[0] != '(' or s[-1] != ')':
        return False

    return nest_paren(s[1:-1])



if __name__ == "__main__":
    


    s = "((()))8"


    print(nest_paren(s))
