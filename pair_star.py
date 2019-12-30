

def rabin_karp(s1,s2):

    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    x = 53

    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = False

        current_hash = cur

def pair_star(s):
    if len(s) <= 1:
        return s

    return (s[0] + "*" if s[0] == s[1] else s[0]) + pair_star(s[1:])


if __name__ == "__main__":
    

    print(pair_star("hello"))
