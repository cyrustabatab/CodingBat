



def rabin_karp(s1,s2):

    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    x = 53
    same = True


    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = False

        current_hash = current_hash * x + ord(s1[i])
        target_hash = target_hash * x + ord(s2[i])

    if same:
        return 0

    power = x**(len(s2) - 1)

    for i in range(len(s2),len(s1)):
        letter_to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter_to_remove)) * x + ord(letter_to_add)
        if current_hash == target_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1

    return -1



if __name__ == "__main__":
    
    s1 = "hello"
    s2 = "lo"

    print(rabin_karp(s1,s2))
