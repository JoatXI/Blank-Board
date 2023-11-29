# implementation of merge sort algorithm

import random

def sorter(nums):
    print(nums)
    # checking if the array is empty or contains one element
    if len(nums) <= 1:
        return nums
    
    # get the mid point of the array
    mid = len(nums) // 2
    
    # split the list into two halves,
    # sorts each half of the array recursively
    # and combine or merge the results of the two halves
    return merger(sorter(nums[:mid]), sorter(nums[mid:]))

def merger(left, right):
    #print(left, right)
    i, j, merged_arr = 0, 0, []
    # iterate over each element of the left and right arrays
    while i < len(left) and j < len(right):
        # check if the current element in the left array is
        # is less than or equal to the current element in the right array
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
    
    # returns the merged array and adds any remainder of each array if any
    return merged_arr + left[i:] + right[j:]

nums = [i for i in range(20)]
random.shuffle(nums)

result = sorter(nums)
print(result)