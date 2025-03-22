nums = [1, 3, 8, 9]

target = 10
# sum = 0
# i = 0
# for num in nums:
#     sum = num + nums[i + 1]
#     if sum != target:
#         sum = 0
#         i += 1
#     else:
#         print("[" + str(num) + "," + str(nums[i + 1]) + "]")
        
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1

# output: [1, 2]
# nums[1] + nums[2] = target = 10
print(twoSum(nums, target))