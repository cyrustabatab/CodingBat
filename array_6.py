



def array6(nums,index):
    if index == len(nums):
        return False

    if nums[index] == 6:
        return True

    return array6(nums,index + 1)


