


memo = {} 
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        

        value =  (fibonacci(n - 1) if n -1 not in memo else memo[n -1]) + (fibonacci(n -2) if n -2 not in memo else memo[n -2])

        memo[n] = value

        return value





if __name__ == "__main__":
    

    print(fibonacci(7))

    print(memo)
