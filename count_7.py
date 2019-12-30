



def count7(n):
    if not n:
        return 0
    
    
    return (1 if n % 10 == 7 else 0) + count7(n//10)


if __name__ == "__main__":
    

    print(count7(777727))
