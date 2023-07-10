'''
que-
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''
'''approach: 
Greedy soln: O(n) TC and O(1) SC
track in reverse order and check if prev value can reach to current value, if yes move one step 
in backward order and keep on checking by shifting the goal post.
here the num at index i represents how many jumps can be taken if it is 2 it can take either 1 or 2 jump
if its 4 it can take 1,2,3,4 jumps
if it's 0 it can take no jump to reach endgoal
'''
'''
approach-
Base case: last index can trivially reach to last index.
Q1: How can I reach to the last index (I will call it last_position) from a preceding index?
If I have a preceding index idx in nums which has jump count jump which satisfies
 idx+jump >= last_position, I know that this idx is good enough to be treated as the last 
 index because all I need to do now is to get to that idx. I am going to treat this new idx 
 as a new last_position.
 So now, here are two important things:

If we have indices which are like sinkholes, those with 0 as jump and every other preceding index can only jump to that sinkhole, our last_position will not be updated anymore because idx+jump >= last_position will not be satisfied at that sinkhole and every other preceding index cannot satisfy the idx+jump >= last_position condition since their jumps are not big enough.
E.g. nums=[3,2,1,0,4] # Here 0 is a sinkhole becuase all preceding indices can only jump to the sinkhole
If we have barriers, those indices with 0 as jump, but the preceding indices contain jumps which can go beyond those barriers, idx+jump >= last_position will be satisfied and last_position will be updated.
E.g. nums=[3,2,2,0,4] # Here 0 is just a barrier since the index before that 0 can jump *over* that barrier
Finally ask this question when we have finished looping

Is the last position index of 0? (i.e, have we reached to the beginning while doing the process of jumping and updating the last_position?)
If we have sinkholes in nums, our last_position will not be 0. Thus, False will be retured.
'''
def jump_game(nums):
    goal=len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        z=i+nums[i] #If this index has jump count which can reach to or beyond the last position
        if z>=goal:
            goal=i #Since we just need to reach to this new index
    return True if goal==0 else False

'''approach2
curr = nums[0]
        # Traverse all the elements through loop...
        for i in range(1,len(nums)):
            # If the current index 'i' is less than current maximum jump 'curr'...
            # It means there is no way to jump to current index...
            # so we should return false...
            if curr == 0:
                return False
            curr -= 1
            # Update the current maximum jump...
            curr = max(curr, nums[i])       # It’s possible to reach the end of the array...
        return True
'''
'''approach explained
We can use a pointer j to indicate the farthest index we can reach.
As any index within j can be chosen to jump from, we can use a heuristic that for each index i whose jump length is x, j = max(j, i+x). If i+x > j, we just jump from i to increase our jump range from j to i+x.
But we should ensure that i is reachable
'''
'''
approach 4
We start travering the array from start
While traversing, we keep a track on maximum reachable index and update it accordingly. If we reach the maxium reachable index we get out of loop.
At last, if maxium reachable index is greater than or equal to last index of the array, means we can reach the last element else return false.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = 0
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]
            if curr == reachableIndex:
                break
                
        return reachableIndex >= len(nums) - 1
'''

# nums=[2,3,1,1,4]
nums = [3,2,1,0,4]
result=jump_game(nums)
print(result)