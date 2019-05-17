def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) > 15000:
        return None

    if len(nums) < 3:
        return False
    
    currentMin = nums[0]
    for i in range(1, len(nums)-1):
        if currentMin < nums[i]:
            for j in range(i+1, len(nums)):
                if currentMin < nums[j] < nums[i]:
                    return True
        else:
            currentMin = nums[i]

    return False

def find132patternProb(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 3:
        return False
    curr_min = nums[0]
    for i in range(1, len(nums)-1):
        if curr_min < nums[i]:
            for j in range(i+1, len(nums)):
                if curr_min < nums[j] < nums[i]:
                    return True
        else:
            curr_min = nums[i]
    return False


# print(find132pattern([1, 2, 3, 4]))
# print(find132pattern([3, 1, 4, 2]))
# print(find132pattern([-1, 3, 2, 0]))
print(find132pattern([3,5,0,3,4]))
print(find132patternProb([3,5,0,3,4]))