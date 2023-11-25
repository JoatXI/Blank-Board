# LeetCode's TwoSum hash map solution:

def twoSum(nums, query):
        map = {}
        
        for i, val in enumerate(nums):
            dif = query - val
            if dif in map:
                return [map[dif], i]
            map[val] = i
        return False
    
nums = [3, 2, 4]
query = 6

two_result = twoSum(nums, query)
print(two_result)

# testing bubble sort algorithm:

def bubbleSort(nums):
    
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i + 1], nums[i]
    return nums

nums = [3, 2, 4]
bub = bubbleSort(nums)
print(bub)