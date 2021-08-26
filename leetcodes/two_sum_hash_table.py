def twoSum(nums, target):
    increment_count = 1
    for item in nums:
        for item_two in nums[increment_count:]:
            if (item + item_two) == target:
                return [nums.index(item), nums.index(item_two)]
        increment_count += 1
    return []

print(twoSum([1,2,3,5], 7))
print(twoSum([10,12,13,15], 25))
print(twoSum([1,2,3,5], 10))