
def change_xy(s):
    if not s:
        return ''

    return ('y' if s[0] == 'x' else s[0]) + change_xy(s[1:])

if __name__ == "__main__":
    

    print(change_xy("xxhixx"))
