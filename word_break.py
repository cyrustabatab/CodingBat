


def rabin_karp(s1,s2):

    assert len(s1) >= len(s2)
    current_hash = target_hash = 0
    same = True
    x = 53

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



def min_coin_change(n,denoms):

    minimum = [[0 if i == 0 else float("inf"),None] for i in range(n + 1)] 

    for amount in range(1,n + 1):
        for i,denom in enumerate(denoms):
            if denom <= amount:
                if 1 + minimum[amount - denom][0] < minimum[amount][0]:
                    minimum[amount][0] = 1 + minimum[amount - denom][0]
                    minimum[amount][1] = i



    print(minimum) 
    coins = reconstruct_coins(minimum,denoms)
    
    print(coins)

def reconstruct_coins(minimum,denoms):
    
        
    coins = {denom: 0 for denom in denoms}

    i = len(minimum) - 1

    while True:
        case = minimum[i][1]
        
        if case is None:
            break

        coins[denoms[case]] += 1
        i -= denoms[case]


    return coins






def word_break(sentence,dictionary):
    
    word = []
    word_break_helper(sentence,dictionary,word)


def word_break_helper(sentence,dictionary,word,start=0):


    for i in range(start + 1,len(sentence) + 1):
        prefix = sentence[start:i]
        if prefix in dictionary:
            if i == len(sentence):
                word.append(prefix)
                print(' '.join(word))
                word.pop()
                return
            else:
                word.append(prefix)
                word_break_helper(sentence,dictionary,word,i)
                word.pop()




if __name__ == "__main__":

    n = 125
    denoms = (1,5,10,25)

    
    min_coin_change(n,denoms)


    

