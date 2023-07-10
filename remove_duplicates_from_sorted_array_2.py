#Given an integer array nums sorted in non-decreasing order, 
# remove some duplicates in-place such that each unique element appears at most twice. 
# The relative order of the elements should be kept the same.

def remove_duplicates(nums):
    left=2 #first two number will always be counted so iterate from 3nd number of loop
    for right in range(2,len(nums)):
        if nums[right]!=nums[left-2]: #check two numbers
            nums[left]=nums[right] #place new unique number at index left
            left+=1
    return left

nums = [0,0,1,1,1,1,2,3,3]
result=remove_duplicates(nums)
print(result)