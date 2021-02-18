# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.
#
# Follow up: Could you implement a solution with a linear runtime complexity 
# and without using extra memory?

def singleNumber(nums):
    for num in nums: 
        if (nums.count(num) == 1): 
            return num

        else: 
            continue 


print(singleNumber([2,2,1]))
