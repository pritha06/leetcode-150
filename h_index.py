'''que:
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia:
The h-index is defined as the maximum value of h such that the given researcher has published at
least h papers that have each been cited at least h times.
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
'''
'''The question is quite simple if the citations are sorted. 
Which means we need some kind of "sorting". 
The observation h index is limited by both citation and paper count gives us the idea of 
counting/bucket sort. We can consider any paper with citations larger than n as citation == n.
This way we can sort the citations in O(n) time with O(n) space. 
Time Complexity: O(nlogn), where n is the length of the citations array. This is because we 
need to sort the array in non-increasing order, which takes O(nlogn) time.

Space Complexity: O(1), as we are sorting the array in-place and using only constant extra space.
The rest is trivial.'''
def hIndex(citations):
    citations.sort(reverse=True)
    print(citations)
    for index,citation in enumerate(citations):
        print("index:",index)
        print("citation:",citation)
        if index>=citation:
            return index
    return len(citations)




citations = [3,0,6,1,5]
result=hIndex(citations)
print(result)

'''detailed:
Sort all the citations in descending order. Now iterate through all the citations starting from the largest one. Since we require h papers to have h citations atleast, we keep going onto smaller and smaller number of citations until we reach a point where the index (the number of papers) is greater than the number of citations.

Note that at each point of iteration (until we stop), the number of papers covered so far (starting from the left-most index) are less than the value of the smallest citations encountered so far.
Upon encountering an index that's greater than the number of citations, we can say that it was till the previous index that the constraint (that h number of papers need to have h citations atleast) was satisfied.

Hence it's all the papers till the previous index that we need to count and return. To do that, we can simply return the index at which the constraint breaks, since because the indexing actually starts from 0 (meaning index 5 means we're on the 6th element).

If we never encounter a point where the constraint breaks, then all the papers have very large number of citations (by large I mean the least value of the number of citations is greater than the number of papers themselves).

For example:

[103,102,101,100,99]

Here, there are just 5 papers but the least value of the number of citations is 99.

In this kind of scenario, we need to return the number of paper themselves, because it's for certain then that the number of citations are greater than the number of papers themselves.

So, in the given example, we would return 5.
'''