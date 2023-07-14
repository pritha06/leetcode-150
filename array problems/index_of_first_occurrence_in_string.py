'''Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''
def find_string(haystack,needle):
    needle_len=len(needle)
    haystack_len=len(haystack)
    total=haystack_len-needle_len+1
    if needle_len==0:
        return 0
    for i in range(total):
        if haystack[i:i+needle_len]==needle:
            return i
    return -1
    # if needle in haystack:
    #     return haystack.index(needle)
    # else:
    #     return -1

haystack = "sadbutsad"
needle = "tsad"
result=find_string(haystack,needle)
print(result)

'''Intuition:
The problem requires us to find the index of the first occurrence of the needle string in the haystack string. We can solve this problem by checking each substring of the haystack that has the same length as the needle, and compare it with the needle to see if they match. If a match is found, return the starting index of the substring, otherwise continue checking the next substring. If no match is found, return -1.

Approach:
Calculate the length of the haystack and needle strings.
If the length of the needle is 0, return 0.
Use a loop to check each substring of the haystack that has the same length as the needle, starting from the first character of the haystack.
Inside the loop, use another loop to compare each character of the substring with the corresponding character of the needle. If a character doesn't match, break the loop and move to the next substring.
If all characters match, return the starting index of the substring.
If no match is found, return -1.
Complexity
Time Complexity: O((n-m+1)m) = O(nm)

Note - In the worst-case scenario, we would have to check all possible substrings of the haystack string that have the same length as the needle string. There are (n-m+1) such substrings. For each substring, we need to compare each character with the corresponding character in the needle string, which takes O(m) time. Therefore, the total time complexity would be (n-m+1)m, which can be simplified to O(nm) since n and m are both variables that can change.
Space Complexity: O(1)
'''