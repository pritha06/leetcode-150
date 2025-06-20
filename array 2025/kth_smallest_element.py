def k_small_element(n,nums,k):
    if n==1:
        return nums[0]
    nums.sort() #sorts in place
    return nums[k-1] #k-1 because of indexing



n=6
nums=[7,10,4,3,20,15]
k=3
print(k_small_element(n,nums,k))
