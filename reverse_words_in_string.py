'''que:
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. 
Do not include any extra spaces.
'''
def reverseWords(s):
    result=''
    i=0 #keep two pointers i and j to mark start of word and end of word in a multiple words string 
    n=len(s)
    while i<n: 
        while i<n and s[i]==' ': #i check for space and increment it until a nonspace is encountered
            i+=1
        if i>=n:
            break
        j=i+1 #j check for word length and increment it until another space is found
        while j<n and s[j]!=' ':
            j+=1
        sub=s[i:j] #sub is the word from i to j where i is start of word, j is end of one word.
        if len(result)==0: #check result length if empty, add only one word to it
            result=sub
        else:
            result=sub+' '+result #check if not empty, add new word then space then result(sequence maintain)
        i=j+1  #loop for another word to check, follow same steps 
    return result

    # s=s.split()
    # s.reverse()
    # print(s)
    # res=""
    # for i in s:
    #     res+=(i+" ")        
    # return res.rstrip()    
    

    


s = "  hello world  "
result=reverseWords(s)
print(result)