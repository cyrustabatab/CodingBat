



def count_8(n):
    if n == 0:
        return 0

    return (2 if n % 10 == 8 and (n//10) % 100 == 8 else 1 if n % 10 == 8 else 0) + count_8(n//10)


