'''
que:
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i.
Return the minimum number of jumps to reach nums[n - 1]. 
'''
'''
Explanation to Approach :
We are using a search algorithm that works by moving forward in steps and counting each step as a jump.
The algorithm keeps track of the farthest reachable position at each step and updates the number of jumps needed to reach that farthest position.
The algorithm returns the minimum number of jumps needed to reach the end of the array.
Complexity :
Time complexity : O(n)
Space complexity: O(1)
'''
def jump(nums):
    ans=0
    end=0
    farthest=0
    for i in range(len(nums)-1):
        farthest=max(farthest,i+nums[i])
        if farthest>=len(nums)-1:
            ans+=1
            break
        if i==end: # Visited all the items on the current level
            ans+=1 # Increment the level
            end=farthest # Make the queue size for the next level
    return ans
'''The idea is that we only jump when we absolutely have to, this way the total number of jumps will be minimized.'''
'''size = len(nums)
        
        # destination is last index
        destination = size - 1
        
        # record of current coverage, record of last jump index
        cur_coverage, last_jump_index = 0, 0
        
        # counter for jump
        times_of_jump = 0
        
         # Quick response if start index == destination index == 0
        if size == 1:
            return 0
        
        
        # Greedy strategy: extend coverage as long as possible with lazy jump
        for i in range( 0, size):
            
            # extend current coverage as further as possible
            cur_coverage = max( cur_coverage, i + nums[i] )
            

            # forced to jump (by lazy jump) to extend coverage  
            if i == last_jump_index:
            
                # update last jump index
                last_jump_index = cur_coverage
                
                # update counter of jump by +1
                times_of_jump += 1
                
                # check if reached destination already
                if cur_coverage >= destination:
                        return times_of_jump
                
        return times_of_jump
        '''
# nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
result=jump(nums)
print(result)