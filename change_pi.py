



def change_pi(s):

    if len(s) < 2:
        return s

    return ("3.14" + change_pi(s[2:])) if s[:2] == 'pi' else (s[0] + change_pi(s[1:]))



if __name__ == "__main__":
    

    print(change_pi("xpix"))


