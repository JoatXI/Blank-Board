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