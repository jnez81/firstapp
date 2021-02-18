# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotateArray(nums, k):
    
    counter = 0
    while (counter < k):
        lastElement = nums.pop()
        nums.insert(0, lastElement)
        counter += 1

    return nums

print(rotateArray([1,2,3,4,5,6,7], 3))