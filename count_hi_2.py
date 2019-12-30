




def count_hi_2(s):

    if len(s) <= 1:
        return 0

    if s[0] == 'x' and s[:3] == 'xhi':
        return count_hi_2(s[3:])
    elif s[:2] != 'hi':
        return count_hi_2(s[1:])
    else:
        return 1 + count_hi_2(s[2:])
        



if __name__ == "__main__":
    

    print(count_hi_2("ahixhi"))
