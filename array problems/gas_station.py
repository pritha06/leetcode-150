'''que:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to
its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index 
if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique
'''
'''approach:
There are 4 parts to it-

Part 1- sum of gas array>=sum of cost array---> 
very intuitive, we should always have enough gas.

Part 2- we are keeping a total+=gas[i]-cost[i] for each i, and whenever it is <0 we are skipping that point and moving forward, making total 0--->
 It means we ran out of gas if we started at some point which was <= current pos of i, so now we have to find a new starting position,
which wall be > curr pos of i.
Now think, why will this new start lie ahead of curr pos i, not anywhere before it,  you could think, we started from point A------>B(total till +ve)------->C(total<0), as per this algo we try to find start ahead of C, what if we started from B and skipped A instead, well that won't work, You moved from A--------> B with some positive value(or 0), or else you would have stopped right at B and made total to 0. So add A improved our chances of having a positive total, so there is no point in looking for the new position start anywhere behind point C.

Part 3- When the total stays +ve, we dn't do anything to the start point, our start pointer points to the first index when our total became positive.
Again this is similar to the above explanation-l
ets suppose we start from X(-ve)--->Y(-ve)--->A(+ve)---->B(+ve)---->C(+ve), where C is the end of the array, our start(which is also the ans) would be A.
Why not B? why not C?
It is because we moved from A to B with some +ve value or atleast 0, whereas if we started from B we would have had only the value of B so earlier point added some value to our total, so its more favorable to help us reach the ans, hence earliest point is always better.

Part 4-- Why we just stop at point C and don t complete the cycle and check.
It is because from Part 1 we would have already identified that if the given set of inputs will have an ans, so if we have reached to Part 3 it means we surely have an ans, and it is mentioned in the question that there is only one valid ans, so we will always choose the most favorable ans-- which is also the fundamental idea of Greedy Algorithims. There is also a mathematical proof for this, that if we got a start point given our total gas >=total cost , we will be able to reach back to that point with just enough gas. 
'''

'''best explanation-
https://leetcode.com/problems/gas-station/solutions/1004074/greedy-method-explanation-visual-python/?envType=study-plan-v2&envId=top-interview-150
'''
def find_way(gas,cost):
    if sum(gas)<sum(cost):
        return -1
    total=0
    start=0
    for i in range(len(gas)):
        total+=gas[i]-cost[i]
        if total<0:
            start=i+1
            total=0
    return start

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
result=find_way(gas,cost)
print(result)

'''Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.'''