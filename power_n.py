



def powerN(base,n):
    if n == 0:
        return 1

    return base * powerN(base,n - 1)




if __name__ == "__main__":
    

    print(powerN(2,5))
