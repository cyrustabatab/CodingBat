



def str_copies(s,sub,n):

    if n == 0:
        return True

    if len(s) < len(sub):
        return False

    if s[:len(sub)] == sub:
        return str_copies(s[1:],sub,n - 1)
    else:
        return str_copies(s[1:],sub,n)
    





if __name__ == "__main__":
    

    print(str_copies("catcowcat", "cat", 2))
