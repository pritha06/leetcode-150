'''que:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without using the division operation.
'''
'''approach:
Solution 1: Maintaining Prefix and Suffix Array 
Approach:

In this approach, we will use two extra arrays and maintain prefix and suffix products up to the current index. Let’s understand using an array.
index- 0 1 2 3 4
Arr = { 1 , 4 , 6 , 2 , 3}       N=5
Prefix Arr ={ 1 , 1 , 4 , 24 , 48 } (runs from first to end, first always 1)
Suffix Arr ={ 144 , 36 , 6 , 3 , 1 } (runs from end to first, last always 1)
For obtaining Prefix Array, Start from the first Index and multiply element one by one and store it in an array. Similarly, for obtaining a Suffix Array, Start from the end and multiply elements one by one, and store them in an array. Now moving on to every index, take the product of prefix and suffix Array to get the product of the whole array except itself.
prefix[i]=prefix[i-1]*arr[i-1]
suffix[i]=suffix[i+1]*arr[i+1]
Using them to compute the product Array (Having product of the whole array except the element itself)
res[i]=prefix[i]*suffix[i]
Time Complexity: O(n)

Space Complexity: O(n) + O(n)
code
prefix=[1]*len(nums)
suffix=[1]*len(nums)
res=[1]*len(nums)
for i in range(1,len(nums)):
    prefix[i]=prefix[i-1]*nums[i-1]

for i in range(len(nums)-2,-1,-1):
    suffix[i]=suffix[i+1]*nums[i+1]

for i in range(0,len(nums)):
    res[i]=prefix[i]*suffix[i]

return res
Solution 2: It is just a further optimized version without using Suffix Array.

We will create a prefix Array and then after that instead of creating a suffix array separately, start from the end of the array and maintain a variable suffixproduct which will keep track of the suffix product up to the current index.
'''
def productExceptSelf(nums):
    res=[1]*len(nums) #res array
    prefix=1
    for i in range(len(nums)): #prefix array stored
        res[i]=prefix
        prefix*=nums[i]

    postfix=1
    for i in range(len(nums)-1,-1,-1): #suffix sum array stored
        res[i]*=postfix #add existing left product value to right one
        postfix*=nums[i]
    
    return res
'''TC: O(n), SC:O(1)//constant size
'''

nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
result=productExceptSelf(nums)
print(result)