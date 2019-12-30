



def bunnyEars2(bunnies):
    if bunnies == 0:
        return 0
    else:
        return (2 if bunnies % 2 else 3) + bunnyEars2(bunnies -1)



