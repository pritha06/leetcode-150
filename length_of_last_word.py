'''Given a string s consisting of words and spaces, return the length of the last word in the string'''
def lengthOfLastWord(s):
    """
        The single O(n) loop solution!
        The answer must be less than or equal to len(s)
        
        The trick is to iterate backwards!
        We want to keep iterating until we either hit a space (after finding the last word)
        or if we reached the end of the word with no space (meaning there is only on word)
        """
    length=0
    letter_found=False
    for i in range(len(s)-1,-1,-1):
        if s[i]!=' ':
            letter_found=True
            length+=1
        # account for edge case that no spaces, means just a single word
        if letter_found==True and (s[i]== ' ' or i==0):
            return length
    return 0

    

'''
using split:
z=s.split()
return len(z[-1])
'''
        
# s = "Hello World"
s="   fly me   to   the moon  "
length=lengthOfLastWord(s)
print(length)
