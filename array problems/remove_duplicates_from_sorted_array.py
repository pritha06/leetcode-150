def remove_duplicates(nums):
    x=1 #first number will always be unique so iterate from 2nd number of loop
    for i in range(len(nums)-1):
        if nums[i]!=nums[i+1]: #check two consecutive numbers
            nums[x]=nums[i+1] #place new unique number at index 
            x+=1
    return x

#Given a sorted array and we need to return the length of the unique elements instead of the entire array. 
# There is no need to delete the duplicate elements also.
# Since, our first element is already present at index 0 (it is a unique element), we quickly run a for loop for the entire array 
# to scan for unique elements.
# If the current element and the next element are the same, then we just keep on going till we find a different element
# Once we find a different element, it is inserted at index 1, because, index 0 is taken by the first unique element.
# Once this is done, the same scanning is done to find out the next unique element and this element is to be inserted at index 2.
#  This process continues until we are done with unique elements.
# We use a variable (x = 1) which is incremented to the next index whenever we find a unique element and we insert this element at its 
# corresponding index.
nums = [0,0,1,1,1,2,2,3,3,4]
result=remove_duplicates(nums)
print(result)