




def countX(s):
    if not s:
        return 0

    return (s[0] == 'x') + countX(s[1:])




if __name__ == "__main__":
    

    print(countX('xhixhix'))
