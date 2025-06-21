def threesum(nums):
    res=[]
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]: #checking first i value
            continue
        else:
            l=i+1
            r=len(nums)-1
            while l<r:
                subtotal=nums[i]+nums[l]+nums[r]
                if subtotal==0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]: #to check duplication of l and r also they shouldn't be equal
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif subtotal<0:
                    l+=1
                else:
                    r-=1
    return res
        
        

nums=[-1,0,1,2,-1,-4]
print(threesum(nums))