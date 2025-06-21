#no sorting because we want -ve numbers in sequence only
#constand space soln with O(n) time complexity
def move_negative(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]<0:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            j+=1
    return nums
    

nums=[2,-3,4,5,6,-7,8,9]
print(move_negative(nums))
