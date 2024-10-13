def heapSort(nums):
    for i in range(len(nums) // 2 - 1, -1, -1):
        heapify(nums, len(nums), i)
    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    return nums

def heapify(nums, n, i):
    left, right, largest = 2 * i + 1, 2 * i + 2, i
    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest!= i:
        nums[largest], nums[i] = nums[i], nums[largest]
        heapify(nums, n, largest)

nums = [3, 2, 4, 15, 3, 81, 0, 8, 48, 4, 9, 6, 7, 47, 13, 23]
heapo = heapSort(nums)
print(heapo)