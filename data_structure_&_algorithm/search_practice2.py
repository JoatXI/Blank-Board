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
       
    # trying to implement a much more optimal approach with al algorithm that is less than 0(N^2) time complexity..
        # create an empty list that will later take in the indices
        # create two variables start_point and end_point with the values 0 and len(nums) -1 respectively that tracks the start and end point of the array
        # sort the list
        # get the first number by getting the midpoint of list
        # check if the sum of the current number and the number at the next index is equal to the target
        # if it is, return the index of both numbers
        # if it isn't, check if the sum of the current numbers is less than target and adjust the search area to the right of the array
        #if it is greater than the target then move search area to the left
        
        
def binary_search(nums, target):
    start_point, end_point = 0, len(nums) - 1
    
    while start_point <= end_point:
        mid_point = (start_point + end_point) // 2
        mid_point_value = nums[mid_point]
        
        if mid_point_value == target:
            return mid_point
        elif mid_point_value < target:
            start_point += 1
        elif mid_point_value > target:
            end_point -= 1
            
    return -1

def two_sum(nums, target):
    for i, j in enumerate(nums):
        second_value = target - j
        
        second_index = binary_search(nums, second_value)
        
        if second_index != -1 and second_index != i:
            return [i, second_index]
        
    return []

           
nums = [3, 2, 4]
target = 6

brute_result = brute_two_sum(nums, target)
binary_result = two_sum(nums, target)
print(brute_result)
print(binary_result)