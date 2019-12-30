
def count_hi(s):

    if not s:
        return 0

    return (1 + count_hi(s[2:])) if s[:2] == 'hi' else (count_hi(s[1:]))

if __name__ == "__main__":
    

    print(count_hi("hihih"))
