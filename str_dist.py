


def str_dist(s,sub):

    if len(s) < len(sub):
        return 0


    if s[:len(sub)] == sub and s[-len(sub):] == sub:
        return len(s)
    
    if len(s) == len(sub):
        return 0

    if s[:len(sub)] == sub:
        return str_dist(s[:-1],sub)
    elif s[-len(sub):] == sub:
        return str_dist(s[1:],sub)
    else:
        return str_dist(s[1:-1],sub)




if __name__ == "__main__":
    
    print(str_dist("cccatcowcatxx", "cat"))

