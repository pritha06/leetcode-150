#if only 1 element in nums then return that only because its min and max both
#
def find_sum(N,nums):
    # min_element=min(nums)
    # max_element=max(nums)
    # sum_nums=min_element+max_element
    # return sum_nums
    if len(nums)==1:
        return nums[0]
    if nums[0]>nums[1]:
        mini=nums[1]
        maxi=nums[0]
    else:
        mini=nums[0]
        maxi=nums[1]
    for i in range(2,N):
        if nums[i]>maxi:
            maxi=nums[i]
        elif nums[i]<mini:
            mini=nums[i]
    return maxi+mini



N=5
nums=[-3,1,-4,5,6]
print(find_sum(N,nums))