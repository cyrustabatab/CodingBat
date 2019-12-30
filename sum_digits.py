


def sumDigits(n):
    if not n:
        return 0

    return n % 10 + sumDigits(n/10)


