"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


def brute_two_sum(nums, target):
    
    # We need to return the indices of two numbers that the some of num1 + num2 = target_value.
    # we need to consider the solution works for every type of list tested

    # What we know:
    #.. consider that there maybe duplicate numbers.. which are fine
    # the list cannot be empty and contains at least two numbers
    # there maybe negative numbers in the list
    # the sum of two numbers cannot be a sum of the same number, unless it's a duplicate number
    # also the target number can possibly be a negative integer

    # first try to implement a linear search approach
    # create an index variable with the value 0
    # create a empty list that will later take in the index values
    # check if the sum of the current number and the number at the next index is equal to the target
    # if it is, return the index of both numbers
    # if it isn't, increase index by 1 and move to the next index until it gets to the end of the list
    # return nothing if its not found
    # assume it is an unsorted list as there's no mention of the array being sorted or not
    
    # creating index variable and empty result list
    """
    position = 0
    result_list = []
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                print("index1:", i, "value1:", nums[i], "index2:", j, "value2:", nums[j])
                result_list.append(i)
                result_list.append(j)
                return result_list
        
            position += 1
            
    """
    
def two_sum(nums, target):
    pass
           
nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 26

result = brute_two_sum(nums, target)
print(result)