#The majority element is the element that appears more than ⌊n / 2⌋ times. 
#You may assume that the majority element always exists in the array.

#-----------approach-1------------
# If we sort the array, the middle element would always be the majority element -- the majority element would overarch more than half of the array.

# Complexity
# Time complexity: O(NLogN) from sorting
# Space complexity: O(1) -- we are not adding extra space.

#code
#nums.sort()
#l=len(nums)        
#m=l//2        
#return nums[m]

#-----approach 2------
#simplified hashmap usage considering majority element is always >n/2
# count={}        
# for num in nums:
#    count[num]=1+count.get(num,0)
#    if (count[num]>len(nums)//2) :
#        return num

# Time and Space = O(N)

#--------approach 3---------
#Boyer Moore algo
#explanation-
"""
            Since the count of majority element will be atleast n//2 + 1 therefore, 
            if we make a number as majorityElement and keep on incrementing the count if we encounter that element again and decrement the count if any other element is encountered then the majority element will have atleast 1 in count. Whenever the count becomes 0, reinitialise the majority element with current number.
            For example, nums = [2,2,1,1,1,2,2]
            Let's say majorityElement is 2 therefore count will be 1.
            Nove move ahead and again 2 is encountered so count will be incremented and become 2.
            Now 1 is encountered so count will be decremented and become 1
            Now again 1 is encountered so count will be decremented and become 0
            Now 1 is encountered but count is 0 so initialize 1 as majority element and count to 1 again.
            Now 2 is encountered so count will be decremented and become 0
            Now again 2 is encountered but count is 0 so initialize 2 as majority element and count to 1 again.
            Now no more elements are left so just return the majprity element.
"""
#code-
        # count = 0
        # majorElement = None
        # for num in nums:
        #     if count == 0:
        #         majorElement = num
        #     count += 1 if majorElement == num else -1
        # return majorElement

#best soln in TC and SC : 


def majority_element(nums):
    
    count=0
    majority=None
    for num in nums:
        if count==0:
            majority=num
        count+=(1 if majority==num else -1)
    return majority
    


# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
res=majority_element(nums)
print(res)