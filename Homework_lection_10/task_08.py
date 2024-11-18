def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []

nums = [4, 3, 7, 3]
target = 7
result = two_sum(nums, target)
print("Pair found:", result if result else "No pair found")