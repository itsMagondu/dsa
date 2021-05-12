def twoSum(nums, target):
    store = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in store:
          return [store[m], i]
        else:
          store[n] = i
    return []

print(twoSum([1,2,3,5], 7))
print(twoSum([1,2,2,3,5], 4))
print(twoSum([10,12,13,15], 25))
print(twoSum([1,2,3,5], 10))