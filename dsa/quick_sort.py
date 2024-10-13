# implemenation of quicksort algorithm

import random

def quick_sort(nums, start, end):
    print('quicksort', nums, start, end)
    # checks if end has a value then assign it to the last value in the list
    if end is None:
        end = len(nums) - 1
        
    # checks if start is less than the value of end before implementing quicksort recursively
    if start < end:
        # partition funtion divides the array into two parts arround the pivot
        pivot = partition(nums, start, end) # values to the left of pivot will be smaller than values to the right of the pivot
        quick_sort(nums, start, pivot-1) # calls quick_sort and partition on the left of pivot
        quick_sort(nums, pivot+1, end) # calls quick_sort and partition on the right of pivot
        
    return nums
        
def partition(nums, start=0, end=None):
    # checks if end has a value then assign it to the last value in the list
    if end is None: 
        end = len(nums) - 1
        
    # creates 2 pointer variables with the value of start and (end - 1)
    left, right = start, end-1
    
    # checks if left is less than the value of right before comparing values in the list
    while left < right:
        if nums[left] <= nums[end]:
            left += 1
        elif nums[right] > nums[end]:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left] # swaps the value of the left and right index if out of place
            
    # checks if the value on the left index is greater than the pivot
    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left] # swaps the value of the left index and the pivot
        return left
    else:
        return end


nums = [i for i in range(20)]
random.shuffle(nums)

result = quick_sort(nums, start=0, end=None)
print(result)