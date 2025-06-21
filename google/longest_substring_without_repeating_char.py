def longest_susbtring(s):
    hashmap={}
    if len(s)==0:
        return 0
    max_len=start=0
    for i in range(len(s)):
        if s[i] in hashmap and start<=hashmap[s[i]]:
            start=hashmap[s[i]]+1
        else:
            max_len=max(max_len,i-start+1)
        hashmap[s[i]]=i
    return max_len

s="abacaba"
print(longest_susbtring(s))