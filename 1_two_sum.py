def two_sum(nums: List[int], target: int):
    num_map = {} # store numbers and their indices

    for i, num in enumerate(nums):
        complement = target - num # calculate the number that would be needed to reach target
        if complement in num_map: #
            return [num_map[complement], i]
        num_map[num] = i

    return  []

print(two_sum([2,7,11,15], 9))
