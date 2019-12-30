


def array220(nums,index):

    if index == len(nums) - 1:
        return False

    if nums[index +1] == nums[index] * 10:
        return True

    return array220(nums,index + 1)



