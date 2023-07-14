#----approach-------
#We are given two sorted arrays nums1 and nums2 of sizes m and n, respectively.
#We need to merge these two arrays into a single sorted array, and the result should be stored 
#inside nums1. Since nums1 is of size m+n, we can use this extra space to store the merged array.


#-----approach1 using STL--------
# Traverse through nums2 and append its elements to the end of nums1 starting from index m.
# Sort the entire nums1 array using sort() function.
#TC: O((m+n)log(m+n)) due to sort function, SC:O(1)

#-------approach2 using two pointers------
#We can iterate through the arrays from the end and place the larger element in the end of nums1.
#We can start with two pointers i and j, initialized to m-1 and n-1, respectively.
#We will also have another pointer last initialized to m+n-1, which will be used to keep track of
#the position in nums1 where we will be placing the larger element. 
#Then we can start iterating from the end of the arrays i and j, 
#and compare the elements at these positions. 
#We will place the larger element in nums1 at position last,
# and decrement the corresponding pointer i or j accordingly. 
# We will continue doing this until we have iterated through all the elements in nums2. 
# If there are still elements left in nums1, 
# we don't need to do anything because they are already in their correct place.
#TC: O(m+n) We are iterating through both arrays once, SC:O(1)

def merge(nums1, m, nums2, n):
    last=m+n-1 
    i=m-1
    j=n-1
    while j>=0:
        if i>=0 and nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1
    


#----------TC1---------
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
#-----------TC2--------
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
#-----------TC3--------
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
merge(nums1,m,nums2,n)
print(nums1)

#TC: O(m+n), SC:O(1)