#if we use n.sort() time complexity is O(nlogn), but we want 0(n)
#take 3 variables initialise them to 0 
#run a loop from 0 to N
#put checks if 0 then increase variable count
#multiple while loops until count decreases to 0 and change nums index accordingly
#while loop constant time chalega and for loop N times to N+c+C+C=N

def sort012(n,nums):
    cnt0=0
    cnt1=0
    cnt2=0
    for i in range(n):
        if nums[i]==0:
            cnt0+=1
        elif nums[i]==1:
            cnt1+=1
        elif nums[i]==2:
            cnt2+=1
    i=0
    while cnt0>0:
        nums[i]=0
        cnt0-=1
        i+=1
    while cnt1>0:
        nums[i]=1
        cnt1-=1
        i+=1
    while cnt2>0:
        nums[i]=2
        cnt2-=1
        i+=1
    return nums



n=5
nums=[0,2,1,2,0]
print(sort012(n,nums))