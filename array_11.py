



def array_11(nums,index):

    if index == len(nums):
        return 0

    return (1 if nums[index] == 11 else 0) + array_11(nums,index + 1)
