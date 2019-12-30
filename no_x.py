


def no_x(s):

    if not s:
        return ''

    return ('' if s[0] == 'x' else s[0]) + no_x(s[1:])



if __name__ == "__main__":
    
    s = "xaxb"
    print(no_x(s))
