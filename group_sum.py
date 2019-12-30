


def rabin_karp(s1,s2):
    assert len(s1) <= len(s2)

    same = True
    current_hash = target_hash = 0
    x = 53

    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = False

        current_hash = current_hash * x + ord(s1[i])
        target_hash = target_hash * x + ord(s2[i])

    if same:
        return 0


def min_coin_change(n,denoms): 

    minimum = [[0 if i == 0 else float("inf"),None] for i in range(n + 1)]


    for amount in range(1,n + 1):
        for i,denom in enumerate(denoms):
            if denom <= amount:
                if 1 + minimum[amount- denom][0] < minimum[amount][0]:
                    minimum[amount][0] = 1 + minimum[amount - denom][0]
                    minimum[amount][1] = i

    

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



def group_sum(nums,target):

    current_sum = 0
    
    return group_sum_helper(nums,target,0,current_sum)


def group_sum_helper(nums,target,start,current_sum):

    if current_sum == target:
        return True

    if start == len(nums):
        return False

    
    for i in range(start,len(nums)):
        num =nums[i]
        if current_sum +num <= target:
            current_sum += num

            if group_sum_helper(nums,target,i + 1,current_sum):
                return True


            current_sum -= num

    return False



def group_sum_2(nums,start,target):
    if target == 0:
        return True
    if start == len(nums):
        return False
    
    num = nums[0]
    return group_sum_2(nums,start + 1,target - num) or group_sum_2(nums,start + 1,target)





if __name__ == "__main__":
    
    denoms = (1,5,10)

    n = 13

    print(min_coin_change(n,denoms))

