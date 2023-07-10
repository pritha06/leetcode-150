#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#We have k is 3, so it means we have to take 3 values from the back and put in the front of the array values.
#in order to rotate this Array k times what we will do is, we will reverse the P1 first which become [4,3,2,1] & then we reverse P2 which becomes [7,6,5]
#Now finally what we have to do is we gonna reverse the complete array by doing that what will happen is our array become [5,6,7,1,2,3,4] and that's what we want in our Output
# if we have k = 101, then we will not rotate it 101 times.do the modulo of "k" with length of array
#if k=-ve , add it to length and then do the same steps

'''
we begin by reversing the whole list. After that, the first k elements will be last k elements
 of our original list, but they will be in reverse order. Similarly, the new end of our list 
 will be the old beginning, only in reverse order. So how do we remedy this? Well, we can 
 reverse the first k elements of our new array and the last n-k elements! After that, 
 the array will be fully rotated!
'''
#ANALYSIS :-

# Time Complexity :- BigO(N)

# Space Complexity :- BigO(1)


def rotate_array(nums,k):
    def reverse(left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

    k=k%len(nums)
    if k<0:
        k+=len(nums)
    reverse(0,len(nums)-k-1)
    reverse(len(nums)-k,len(nums)-1)
    reverse(0,len(nums)-1)
    print("nums after rotation",nums)

#approach-2-brute force-Time: O(n•k), Space: O(1) 
'''rotating nums by 1 step, a total of k times. 
the inner part of our outer for loop rotates nums by one spot.
We perform this operation k times to rotate by a total of k steps!
this results in a time limit exception :( so instead of rotating one step at a time, 
let's try to rotate k steps at a time using a second array for extra storage!
'''
'''code-
def rotate_array(nums,k):
    n=len(nums)
    for i in range(k):
        prev=nums[-1]
        for i in range(n):
            nums[i],prev=prev,nums[i]
    print("nums after rotation",nums)
'''

'''approach3-Copy Array; Time: O(n), Space; O(n)
 an element at index i will need to be at index (i + k) % n after our rotation!
  So we can use our second array to simply set every element in nums to be their new value.
'''
'''code-
copy = [num for num in nums] # copy the nums array
n = len(nums)
for i, num in enumerate(copy): # for every element in the copy
	nums[(i + k) % n] = copy[i] # set corresponding location in nums
'''

'''approach4-Pythonic; Time: O(n), Space: O(n)
This solution also takes O(n) time and space since we still 
look at every element once and we also need extra space temporarily for nums[-k:] and nums[:-k]
 if we set nums = nums[-k:] + nums[:-k], then we will actually be creating a new pointer for nums
 in memory. Since we want to actually set nums to this result, we need to set 
 nums[:] = nums[-k:] + nums[:-k], which will overwrite nums element by element.
'''
'''code:
n = len(nums) # store length
k %= n # avoid unnecessary rotations
nums[:] = nums[-k:] + nums[:-k] # set nums to answer
'''
nums = [1,2,3,4,5,6,7]
k = 3
# nums = [-1,-100,3,99]
# k = 2
print("nums before rotation",nums)
rotate_array(nums,k)
