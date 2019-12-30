



def end_x(s):

    if not s:
        return s


    return (end_x(s[1:]) + s[0] if s[0] == 'x' else s[0] + end_x(s[1:]))



if __name__ == "__main__":
    

    print(end_x("xhixhix"))
