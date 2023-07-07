#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# Change the array nums such that the first k elements of nums contain the elements which are not 
# equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Time Complexity: The time complexity of this approach is O(n) since we are traversing the entire array once.
# Space Complexity: The space complexity of this approach is O(1) since we are not using any additional space.

def remove_element(nums,val):
    l=len(nums)
    #two pointer approach, one keep track of int not equal to val, other iterates through loop to check if int is equal to val, if it is skip the check, if not assign the left index to right value.
    left=0
    #replace 
    for right in range(l):
        if nums[right]!=val:
            nums[left],nums[right]=nums[right],nums[left] #to make sure that if no val is present left and right are equal
            left+=1 #returns count of int not equal to val
    return left

#approach described
# The approach taken here is to keep a counter variable count for keeping track of elements other than val and then loop through all the elements of the array. For each element, if it's not equal to val,
#  it is placed at index count of the array, and count is incremented.
# Finally, the length of the new array is equal to count. 
# This approach modifies the input array in-place without using any additional space.
#TC1
# nums = [3,2,2,3]
# val = 3
#TC2
nums = [0,1,2,2,3,0,4,2]
val = 2
result=remove_element(nums,val)
print(result)
