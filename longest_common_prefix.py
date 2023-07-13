'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""
'''

'''approach1-
TC: O(nm ) where m is number of strings and n is length of minimum string in list.
'''
def longest_string(strs):
    result=""
    for i in range(len(strs[0])): #run loop for first string element length
        for s in strs: #run loop for every string in list
            if len(s)==i or s[i]!=strs[0][i]: #if len of new string is done or if the element is not equal to next one return the result
                return result
        result+=strs[0][i] #else add the i character of first string in result
    return result



    '''approach2-
    # result=""
    # l=(list(zip(*strs)))
    # for i in l:
    #     if len(set(i))==1:
    #         result+=i[0]
    #     else:
    #         break
    # return result
    '''


strs = ["flower","flow","flight"]
result=longest_string(strs)
print(result)